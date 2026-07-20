"""
建模能力 2: 基础建模
覆盖Edit Mode操作(挤出/倒角/环切/桥接) + 修改器堆栈(Mirror/Subdivision/Solidify/Boolean/Array)
用法: blender --background --python basic_modeling.py -- --action [extrude|bevel|loopcut|mirror|subdivide|boolean]
"""

import bpy
import sys
import math

def add_cube(size=1, name="Model"):
    bpy.ops.mesh.primitive_cube_add(size=size)
    obj = bpy.context.active_object
    obj.name = name
    return obj


def add_subsurf(obj, levels=2, render_levels=3):
    mod = obj.modifiers.new(name="Subdivision", type="SUBSURF")
    mod.levels = levels
    mod.render_levels = render_levels
    return mod


def add_mirror(obj, axis="X", clipping=True):
    mod = obj.modifiers.new(name="Mirror", type="MIRROR")
    if "X" in axis: mod.use_axis[0] = True
    if "Y" in axis: mod.use_axis[1] = True
    if "Z" in axis: mod.use_axis[2] = True
    mod.use_clipping = clipping
    mod.use_mirror_merge = True
    mod.merge_threshold = 0.001
    return mod


def add_solidify(obj, thickness=0.05):
    mod = obj.modifiers.new(name="Solidify", type="SOLIDIFY")
    mod.thickness = thickness
    return mod


def add_boolean(obj, tool_obj, operation="DIFFERENCE"):
    mod = obj.modifiers.new(name="Boolean", type="BOOLEAN")
    mod.operation = operation
    mod.object = tool_obj
    return mod


def add_array(obj, count=3, offset=(1.5, 0, 0)):
    mod = obj.modifiers.new(name="Array", type="ARRAY")
    mod.count = count
    mod.relative_offset_displace[0] = offset[0]
    mod.relative_offset_displace[1] = offset[1]
    mod.relative_offset_displace[2] = offset[2]
    return mod


def blockout_fox():
    """为狐狸建模搭建初始体块"""
    # 身体
    bpy.ops.mesh.primitive_cube_add(size=1)
    body = bpy.context.active_object
    body.name = "Body"
    body.scale = (0.4, 0.8, 0.35)
    body.location = (0, 0, 0.35)
    add_subsurf(body, 2)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    # 头
    bpy.ops.mesh.primitive_cube_add(size=1)
    head = bpy.context.active_object
    head.name = "Head"
    head.scale = (0.25, 0.3, 0.2)
    head.location = (0, 0.65, 0.55)
    add_subsurf(head, 2)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    # 尾
    bpy.ops.mesh.primitive_cube_add(size=1)
    tail = bpy.context.active_object
    tail.name = "Tail"
    tail.scale = (0.1, 0.6, 0.12)
    tail.location = (0, -0.7, 0.2)
    tail.rotation_euler = (0.3, 0, 0)
    add_subsurf(tail, 2)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    # 前腿(左)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.4)
    fl = bpy.context.active_object
    fl.name = "FrontLeg_L"
    fl.location = (0.12, 0.4, 0.2)
    add_subsurf(fl, 2)

    # 后腿(左)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.06, depth=0.35)
    hl = bpy.context.active_object
    hl.name = "BackLeg_L"
    hl.location = (0.12, -0.4, 0.175)
    add_subsurf(hl, 2)

    for obj in [body, head, tail, fl, hl]:
        obj.select_set(True)

    return body


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    action = argv[1] if len(argv) > 1 else ""

    if action == "fox-blockout":
        blockout_fox()
        print("[OK] Fox blockout created")
    elif action == "cube":
        add_cube()
        print("[OK] Base cube ready")