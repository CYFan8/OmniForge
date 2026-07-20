"""
建模能力 6/11: 渲染引擎 + 批量导出
支持Cycles/Eevee切换, 多格式导出(FBX/OBJ/glTF)
"""

import bpy
import sys
import os


def set_render_engine(engine="cycles", samples=256):
    """切换渲染引擎"""
    scene = bpy.context.scene
    if engine.upper() == "CYCLES":
        scene.render.engine = "CYCLES"
        scene.cycles.samples = samples
        scene.cycles.use_adaptive_sampling = True
        scene.cycles.adaptive_threshold = 0.01
        try:
            prefs = bpy.context.preferences.addons["cycles"].preferences
            prefs.compute_device_type = "CUDA"
            prefs.get_devices()
            for d in prefs.devices:
                if d.type == "CUDA":
                    d.use = True
        except:
            pass
    else:
        scene.render.engine = "EEVEE"
        scene.eevee.taa_render_samples = samples // 4
    print(f"[OK] Engine: {engine}")


def render_still(output_path, resolution=(1920, 1080)):
    """渲染单帧"""
    scene = bpy.context.scene
    scene.render.resolution_x = resolution[0]
    scene.render.resolution_y = resolution[1]
    scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)
    print(f"[OK] Rendered: {output_path}")


def export_model(filepath, fmt="fbx"):
    """导出模型"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    if fmt == "fbx":
        bpy.ops.export_scene.fbx(
            filepath=filepath,
            use_selection=True,
            apply_scale_options="FBX_SCALE_UNITS"
        )
    elif fmt == "obj":
        bpy.ops.export_scene.obj(filepath=filepath, use_selection=True)
    elif fmt == "gltf" or fmt == "glb":
        bpy.ops.export_scene.gltf(
            filepath=filepath,
            export_format="GLB" if fmt == "glb" else "GLTF_EMBEDDED"
        )
    else:
        print(f"[FAIL] Unsupported: {fmt}")
        return
    print(f"[OK] Exported: {filepath}")


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    action = argv[0] if argv else "status"

    if action == "render":
        out = argv[1] if len(argv) > 1 else "./render.png"
        render_still(out)
    elif action == "export":
        out = argv[1] if len(argv) > 1 else "./export.fbx"
        fmt = argv[2] if len(argv) > 2 else "fbx"
        export_model(out, fmt)