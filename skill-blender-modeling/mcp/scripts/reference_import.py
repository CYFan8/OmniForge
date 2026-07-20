"""
建模能力 10: 参考图联动
把外部图片导入Blender视图背景, 支持前/侧/顶正交对齐
用法: blender --background --python reference_import.py -- [--image front.png] [--view front|side|top]
"""

import bpy
import sys
import os


def import_reference(image_path, view="front", opacity=0.5):
    """导入参考图到指定视图"""
    if not os.path.exists(image_path):
        print(f"[FAIL] Image not found: {image_path}")
        return None

    # 根据视图计算位置和旋转
    if view == "front":
        location = (0, -2, 0.5)
        rotation = (0, 0, 0)
    elif view == "side":
        location = (-2, 0, 0.5)
        rotation = (0, math.radians(90), 0)
    elif view == "top":
        location = (0, 0, 2)
        rotation = (math.radians(90), 0, 0)
    else:
        print(f"[FAIL] Unknown view: {view}")
        return None

    import math
    bpy.ops.object.image_add(filepath=image_path, location=location)

    img_obj = bpy.context.active_object
    img_obj.name = f"Ref_{view}"

    mat = bpy.data.materials.new(name=f"RefMat_{view}")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    nodes.clear()
    tex = nodes.new(type="ShaderNodeTexImage")
    tex.image = bpy.data.images.load(image_path)
    bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
    output = nodes.new(type="ShaderNodeOutputMaterial")

    links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    if opacity < 1.0:
        bsdf.inputs["Alpha"].default_value = opacity
        mat.blend_method = "BLEND"

    img_obj.data.materials.append(mat)

    print(f"[OK] Reference image '{view}' -> {image_path}")
    return img_obj


import math

if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []

    for i, arg in enumerate(argv):
        if arg == "--image" and i+1 < len(argv):
            img = argv[i+1]
        if arg == "--view" and i+1 < len(argv):
            vw = argv[i+1]

    img = argv[1] if len(argv) > 1 else None
    vw = argv[2] if len(argv) > 2 else "front"

    if img:
        import_reference(img, vw)