"""
建模能力 1: 项目初始化
创建标准化Blender工程, 设置单位/渲染器/色彩空间/帧率
用法: blender --background --python project_init.py -- [--name MyProject] [--renderer cycles|eevee] [--output ./project.blend]
也可导入使用:
  from scripts.project_init import create_project
  create_project("MyProject", renderer="cycles")
"""

import bpy
import sys
import os
from mathutils import Vector


def create_project(name="untitled", renderer="cycles", output_dir=None):
    """创建标准化Blender工程"""
    bpy.ops.wm.read_factory_settings(use_empty=True)

    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0
    scene.unit_settings.length_unit = "METERS"

    if renderer.upper() == "CYCLES":
        scene.render.engine = "CYCLES"
        try:
            prefs = bpy.context.preferences.addons["cycles"].preferences
            prefs.compute_device_type = "CUDA"
            prefs.get_devices()
            for d in prefs.devices:
                if d.type == "CUDA":
                    d.use = True
        except Exception as e:
            print(f"[WARN] GPU not set: {e}")
        scene.cycles.device = "GPU"
        scene.cycles.samples = 256
    else:
        scene.render.engine = "EEVEE"
        scene.eevee.taa_render_samples = 64

    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.render.fps = 24

    scene.view_settings.view_transform = "AgX"

    if "Cube" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)

    bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
    ground = bpy.context.active_object
    ground.name = "Ground"

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        blend_path = os.path.join(output_dir, f"{name}.blend")
        bpy.ops.wm.save_as_mainfile(filepath=blend_path)
        print(f"[OK] Project created: {blend_path}")

    return scene


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    name = "untitled"
    renderer = "cycles"
    output_dir = None
    for i, arg in enumerate(argv):
        if arg == "--name" and i+1 < len(argv):
            name = argv[i+1]
        elif arg == "--renderer" and i+1 < len(argv):
            renderer = argv[i+1]
        elif arg == "--output" and i+1 < len(argv):
            output_dir = argv[i+1]
    create_project(name, renderer, output_dir)