"""
建模能力 8: 粒子与物理
毛发粒子系统 + 布料/刚体模拟
"""

import bpy
import sys


def add_fur(obj_name, density=5000, length=0.05):
    """给物体添加毛发粒子系统"""
    obj = bpy.data.objects.get(obj_name)
    if not obj:
        print(f"[FAIL] Object '{obj_name}' not found")
        return

    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.particle_system_add()
    psys = obj.particle_systems[-1]
    psys.name = "Fur"

    settings = psys.settings
    settings.type = "HAIR"
    settings.count = density
    settings.hair_length = length
    settings.hair_step = 5
    settings.use_hair_bsdf = True

    # 随机化
    settings.roughness = 0.2
    settings.roughness_endpoint = 0.3
    settings.use_advanced_hair = True

    print(f"[OK] Fur added to '{obj_name}': {density} hairs, length={length}")


def add_cloth(obj_name):
    """给物体添加布料模拟"""
    obj = bpy.data.objects.get(obj_name)
    if not obj: return
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_add(type="CLOTH")
    print(f"[OK] Cloth simulation added to '{obj_name}'")


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    action = argv[0] if argv else "help"
    if action == "fur":
        add_fur(argv[1] if len(argv) > 1 else "Model")
    print("[OK] Particle module loaded")
