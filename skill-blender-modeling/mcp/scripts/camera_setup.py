"""
建模能力 5: 摄像机与构图
多摄像机预设、景深、构图辅助
用法: blender --background --python camera_setup.py -- [--action setup|add] [--focal 50]
"""

import bpy
import sys
import math


def setup_camera(location=(5, -5, 3), target=(0, 0, 0.5), focal_length=50, name="Main_Camera"):
    """设置摄像机并瞄准目标"""
    bpy.ops.object.camera_add(location=location)
    cam = bpy.context.active_object
    cam.name = name
    cam.data.lens = focal_length
    cam.data.clip_start = 0.1
    cam.data.clip_end = 100

    # 指向目标
    direction = (
        target[0] - location[0],
        target[1] - location[1],
        target[2] - location[2]
    )
    import mathutils
    cam.rotation_euler = mathutils.Vector(direction).to_track_quat("-Z", "Y").to_euler()

    bpy.context.scene.camera = cam
    print(f"[OK] Camera '{name}': focal={focal_length}mm, pos={location}")
    return cam


def add_depth_of_field(camera, focus_obj=None, fstop=2.8):
    """给摄像机添加景深"""
    cam_data = camera.data
    cam_data.dof.use_dof = True
    cam_data.dof.aperture_fstop = fstop
    if focus_obj:
        cam_data.dof.focus_object = focus_obj
    print(f"[OK] DOF: f/{fstop}")


def add_composition_guides():
    """添加三分法构图辅助(在视口显示)"""
    # 在场景中添加一个空对象作为构图参考
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0, 0, 0))
    guide = bpy.context.active_object
    guide.name = "Composition_Guide"
    guide.empty_display_size = 2
    print("[OK] Composition guides added")


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    action = argv[0] if argv else "setup"

    if action == "setup":
        setup_camera()