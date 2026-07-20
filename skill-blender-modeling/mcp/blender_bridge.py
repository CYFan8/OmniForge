# Blender MCP Bridge — 远程调度Blender建模/渲染
# 用法: python blender_bridge.py <command> [args...]
# 命令: init | exec | create | render | export | status

import json
import subprocess
import sys
import os
import shutil
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.json"

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def find_blender(config):
    paths = config["blender"]["search_paths"]
    for p in paths:
        if os.path.exists(p):
            return p
    fallback = config["blender"]["fallback_command"]
    if shutil.which(fallback):
        return fallback
    return None

def run_blender_script(blender_path, script_content, background=True):
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(script_content)
        script_path = f.name
    try:
        cmd = [blender_path]
        if background:
            cmd.append("--background")
        cmd.extend(["--python", script_path])
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return result.returncode, result.stdout, result.stderr
    finally:
        os.unlink(script_path)

def cmd_init():
    config = load_config()
    blender = find_blender(config)
    if blender:
        print(f"[OK] Blender found: {blender}")
        result = subprocess.run([blender, "--version"], capture_output=True, text=True, timeout=10)
        version_line = result.stdout.strip().split("\n")[0] if result.stdout else "unknown"
        print(f"[OK] Version: {version_line}")
        config["blender"]["python_path"] = blender
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        return 0
    else:
        print("[FAIL] Blender not found. Install from blender.org")
        return 1

def cmd_status():
    config = load_config()
    blender = find_blender(config)
    print(f"Blender: {blender or 'NOT FOUND'}")
    print(f"Render Engine: {config['render_defaults']['engine']}")
    print(f"Device: {config['render_defaults']['device']}")
    print(f"Script Linkage: {config['linkage']['script_creation']['enabled']}")
    print(f"Image Linkage: {config['linkage']['image_generation']['enabled']}")

def cmd_exec(script_path):
    config = load_config()
    blender = find_blender(config)
    if not blender:
        print("[FAIL] Blender not found")
        return 1
    with open(script_path, "r", encoding="utf-8") as f:
        script = f.read()
    code, stdout, stderr = run_blender_script(blender, script)
    print(stdout)
    if stderr:
        print(stderr)
    return code

def cmd_create(name, renderer="cycles"):
    config = load_config()
    blender = find_blender(config)
    if not blender:
        print("[FAIL] Blender not found")
        return 1
    script = f'''
import bpy
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.context.scene.unit_settings.system = "METRIC"
bpy.context.scene.unit_settings.scale_length = 1.0
if "{renderer}".upper() == "CYCLES":
    bpy.context.scene.render.engine = "CYCLES"
    prefs = bpy.context.preferences.addons["cycles"].preferences
    prefs.compute_device_type = "CUDA"
    prefs.get_devices()
    for d in prefs.devices:
        d.use = d.type == "CUDA"
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.fps = 24
bpy.context.scene.view_settings.view_transform = "AgX"
output = r"{os.path.join(os.getcwd(), name + '.blend')}"
bpy.ops.wm.save_as_mainfile(filepath=output)
print(f"[OK] Project created: {{output}}")
'''
    code, stdout, stderr = run_blender_script(blender, script)
    print(stdout)
    if stderr:
        print(stderr)
    return code

def cmd_render(blend_file, frame=1, output=None):
    config = load_config()
    blender = find_blender(config)
    if not blender:
        print("[FAIL] Blender not found")
        return 1
    out = output or "./renders/"
    os.makedirs(out, exist_ok=True)
    script = f'''
import bpy
bpy.ops.wm.open_mainfile(filepath=r"{blend_file}")
bpy.context.scene.frame_set({frame})
bpy.context.scene.render.filepath = r"{os.path.abspath(out)}frame_{frame:04d}.png"
bpy.ops.render.render(write_still=True)
print(f"[OK] Rendered frame {frame} -> {{bpy.context.scene.render.filepath}}")
'''
    code, stdout, stderr = run_blender_script(blender, script)
    print(stdout)
    if stderr:
        print(stderr)
    return code

def cmd_export(blend_file, fmt="fbx", output=None):
    config = load_config()
    blender = find_blender(config)
    if not blender:
        print("[FAIL] Blender not found")
        return 1
    out = output or "./exports/"
    os.makedirs(out, exist_ok=True)
    script = f'''
import bpy
bpy.ops.wm.open_mainfile(filepath=r"{blend_file}")
output_path = r"{os.path.abspath(out)}export.{{fmt}}"
if "{fmt}" == "fbx":
    bpy.ops.export_scene.fbx(filepath=output_path)
elif "{fmt}" == "obj":
    bpy.ops.export_scene.obj(filepath=output_path)
elif "{fmt}" == "gltf":
    bpy.ops.export_scene.gltf(filepath=output_path)
else:
    print(f"[FAIL] Unsupported format: {fmt}")
print(f"[OK] Exported: {{output_path}}")
'''
    code, stdout, stderr = run_blender_script(blender, script)
    print(stdout)
    if stderr:
        print(stderr)
    return code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python blender_bridge.py <init|status|exec|create|render|export> [args...]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "init":
        sys.exit(cmd_init())
    elif cmd == "status":
        cmd_status()
    elif cmd == "exec":
        if len(sys.argv) < 3:
            print("Usage: python blender_bridge.py exec <script.py>")
            sys.exit(1)
        sys.exit(cmd_exec(sys.argv[2]))
    elif cmd == "create":
        name = sys.argv[2] if len(sys.argv) > 2 else "untitled"
        renderer = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "--renderer" else "cycles"
        sys.exit(cmd_create(name, renderer))
    elif cmd == "render":
        if len(sys.argv) < 3:
            print("Usage: python blender_bridge.py render <scene.blend> --frame 1 --output ./renders/")
            sys.exit(1)
        blend_file = sys.argv[2]
        frame = 1
        output = None
        for i, arg in enumerate(sys.argv[3:], start=3):
            if arg == "--frame" and i+1 < len(sys.argv):
                frame = int(sys.argv[i+1])
            elif arg == "--output" and i+1 < len(sys.argv):
                output = sys.argv[i+1]
        sys.exit(cmd_render(blend_file, frame, output))
    elif cmd == "export":
        if len(sys.argv) < 3:
            print("Usage: python blender_bridge.py export <scene.blend> --format fbx --output ./exports/")
            sys.exit(1)
        blend_file = sys.argv[2]
        fmt = "fbx"
        output = None
        for i, arg in enumerate(sys.argv[3:], start=3):
            if arg == "--format" and i+1 < len(sys.argv):
                fmt = sys.argv[i+1]
            elif arg == "--output" and i+1 < len(sys.argv):
                output = sys.argv[i+1]
        sys.exit(cmd_export(blend_file, fmt, output))
    else:
        print(f"[FAIL] Unknown command: {cmd}")
        sys.exit(1)
