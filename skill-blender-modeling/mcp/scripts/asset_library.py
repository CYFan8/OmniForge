"""
建模能力 12: 资产库
材质库/模型库/场景预设管理
"""

import bpy
import sys
import os
import json


ASSETS = {
    "materials": {
        "metal": {"color": (0.8, 0.8, 0.8), "roughness": 0.2, "metallic": 1.0},
        "wood": {"color": (0.5, 0.3, 0.1), "roughness": 0.7, "metallic": 0.0},
        "glass": {"color": (1, 1, 1), "roughness": 0.05, "metallic": 0.0, "transmission": 1.0},
        "skin": {"color": (0.9, 0.7, 0.6), "roughness": 0.4, "metallic": 0.0, "sss": 0.1},
        "fox_orange": {"color": (0.83, 0.41, 0.15), "roughness": 0.8, "metallic": 0.0, "sss": 0.08},
        "fox_white": {"color": (0.96, 0.94, 0.90), "roughness": 0.8, "metallic": 0.0},
    },
    "primitives": ["cube", "sphere", "cylinder", "cone", "torus"],
}


def load_material(preset_name):
    """从预设库加载材质"""
    preset = ASSETS["materials"].get(preset_name)
    if not preset:
        print(f"[FAIL] Unknown material: {preset_name}")
        return None

    mat = bpy.data.materials.new(name=f"Asset_{preset_name}")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        c = preset["color"]
        bsdf.inputs["Base Color"].default_value = (*c, 1.0)
        bsdf.inputs["Roughness"].default_value = preset.get("roughness", 0.5)
        bsdf.inputs["Metallic"].default_value = preset.get("metallic", 0.0)
        if "transmission" in preset:
            bsdf.inputs["Transmission Weight"].default_value = preset["transmission"]
        if "sss" in preset:
            bsdf.inputs["Subsurface Weight"].default_value = preset["sss"]
    print(f"[OK] Asset material '{preset_name}' loaded")
    return mat


def list_assets():
    """列出所有可用资产"""
    print("=== Materials ===")
    for name in ASSETS["materials"]:
        print(f"  {name}")
    print("=== Primitives ===")
    for name in ASSETS["primitives"]:
        print(f"  {name}")


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    action = argv[0] if argv else "list"

    if action == "list":
        list_assets()
    elif action == "material":
        load_material(argv[1] if len(argv) > 1 else "metal")
