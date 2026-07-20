"""
建模能力 4: 灯光系统
三点布光自动搭建、HDRI环境光、IES灯光
用法: blender --background --python lighting_setup.py -- [--action three_point|hdri|studio]
"""

import bpy
import sys
import math


def clear_lights():
    """删除场景所有灯光"""
    for obj in bpy.data.objects:
        if obj.type == "LIGHT":
            bpy.data.objects.remove(obj, do_unlink=True)


def three_point_lighting(target_obj=None, intensity=1000):
    """三点布光: Key / Fill / Rim"""
    clear_lights()

    if target_obj:
        center = target_obj.location
    else:
        center = (0, 0, 0.5)

    # Key Light - 左上45度
    bpy.ops.object.light_add(type="AREA", location=(
        center[0] - 2, center[1] + 2, center[2] + 2
    ))
    key = bpy.context.active_object
    key.name = "Key_Light"
    key.data.energy = intensity
    key.data.color = (1, 0.95, 0.9)
    key.rotation_euler = (math.radians(45), 0, math.radians(45))
    key.data.size = 1.5
    key.data.shape = "RECTANGLE"
    key.data.size_y = 1.0

    # Fill Light - 右下补光
    bpy.ops.object.light_add(type="AREA", location=(
        center[0] + 1.5, center[1] - 1.5, center[2] + 0.5
    ))
    fill = bpy.context.active_object
    fill.name = "Fill_Light"
    fill.data.energy = intensity * 0.5
    fill.data.color = (0.9, 0.92, 1.0)
    fill.rotation_euler = (math.radians(15), 0, math.radians(-135))
    fill.data.size = 1.0

    # Rim Light - 背后轮廓光
    bpy.ops.object.light_add(type="AREA", location=(
        center[0] + 1, center[1] - 2.5, center[2] + 2.5
    ))
    rim = bpy.context.active_object
    rim.name = "Rim_Light"
    rim.data.energy = intensity * 0.8
    rim.data.color = (1, 0.98, 0.95)
    rim.rotation_euler = (math.radians(45), 0, math.radians(-70))
    rim.data.size = 0.8

    print(f"[OK] Three-point lighting set up (intensity={intensity})")


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    action = argv[0] if argv else "three_point"

    if action == "three_point":
        three_point_lighting()