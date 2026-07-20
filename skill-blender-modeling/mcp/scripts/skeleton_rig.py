"""
建模能力 7: 骨骼动画
骨架快速搭建(四足预设) + 自动蒙皮
"""

import bpy
import sys


def create_armature(name="Armature"):
    """创建并返回骨架"""
    bpy.ops.object.armature_add(location=(0, 0, 0))
    arm = bpy.context.active_object
    arm.name = name
    return arm


def add_simple_bones_from_obj(target_obj, bone_count=5):
    """根据物体形状生成简单骨骼链"""
    bpy.ops.object.select_all(action="DESELECT")
    target_obj.select_set(True)
    bpy.context.view_layer.objects.active = target_obj

    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.armature.bone_primitive_add(name="Root")
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="DESELECT")

    arm = bpy.context.active_object
    if not arm or arm.type != "ARMATURE":
        arm = create_armature()

    arm.location = target_obj.location
    bpy.ops.object.select_all(action="DESELECT")

    target_obj.select_set(True)
    arm.select_set(True)
    bpy.context.view_layer.objects.active = arm

    bpy.ops.object.parent_set(type="ARMATURE_AUTO")
    print(f"[OK] Auto-rigged '{target_obj.name}'")
    return arm


if __name__ == "__main__":
    action = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else None
    print("[OK] Skeleton module loaded")
