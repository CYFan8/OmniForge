"""
建模能力 3: 材质系统
PBR材质工作流, Principled BSDF, 程序化纹理
用法: blender --background --python material_system.py -- [--material fox_fur|glass|metal|skin]
"""

import bpy
import sys


def _get_or_create_material(name, color=(0.8, 0.4, 0.2), roughness=0.5, metallic=0.0):
    """创建或获取材质"""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    bsdf = nodes.get("Principled BSDF")
    if not bsdf:
        bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return mat


def mat_fox_fur(name="Fox_Fur"):
    """狐狸毛皮材质 - 橙+白+黑"""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    bsdf = nodes.get("Principled BSDF")

    # Base color: orange-red
    bsdf.inputs["Base Color"].default_value = (0.83, 0.41, 0.15, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.8
    bsdf.inputs["Subsurface Weight"].default_value = 0.08
    bsdf.inputs["Subsurface Radius"].default_value = (0.02, 0.01, 0.005)
    bsdf.inputs["Subsurface Color"].default_value = (0.9, 0.5, 0.2, 1.0)

    print(f"[OK] Material '{name}' created (fox fur)")
    return mat


def mat_glass(name="Glass"):
    mat = _get_or_create_material(name, color=(1, 1, 1), roughness=0.05, metallic=0.0)
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Transmission Weight"].default_value = 1.0
    bsdf.inputs["IOR"].default_value = 1.45
    return mat


def assign_material(obj_name, mat_name):
    """给对象赋予材质"""
    obj = bpy.data.objects.get(obj_name)
    if not obj: return
    mat = bpy.data.materials.get(mat_name)
    if not mat: return
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    print(f"[OK] Assigned '{mat_name}' to '{obj_name}'")


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    action = argv[0] if argv else "fox_fur"

    if action == "fox_fur":
        mat_fox_fur()
    elif action == "glass":
        mat_glass()