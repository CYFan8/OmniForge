"""
建模能力 13: 高负载降级
算力不足时自动降级策略
"""

import bpy
import sys


def diagnose_performance():
    """诊断当前场景算力需求"""
    total_faces = 0
    total_verts = 0
    for obj in bpy.data.objects:
        if obj.type == "MESH" and obj.data:
            total_faces += len(obj.data.polygons)
            total_verts += len(obj.data.vertices)

    engine = bpy.context.scene.render.engine
    gpu_available = engine == "CYCLES"

    return {
        "faces": total_faces,
        "verts": total_verts,
        "engine": engine,
        "gpu": gpu_available,
    }


def apply_degrade_strategy(strategy="auto"):
    """按策略降级"""
    info = diagnose_performance()
    steps = []

    # 高面数降级
    if info["faces"] > 500000 or strategy == "aggressive":
        for obj in bpy.data.objects:
            if obj.type == "MESH":
                for mod in obj.modifiers:
                    if mod.type == "SUBSURF":
                        mod.levels = max(0, mod.levels - 1)
        steps.append("Subsurf levels reduced")

    # Cycles -> Eevee
    if strategy == "aggressive" or (strategy == "auto" and info["faces"] > 200000):
        if bpy.context.scene.render.engine == "CYCLES":
            bpy.context.scene.render.engine = "EEVEE"
            steps.append("Engine switched: Cycles -> Eevee")

    # 降低采样
    if strategy == "aggressive":
        bpy.context.scene.cycles.samples = 64
        steps.append("Samples reduced to 64")

    if strategy == "minimal":
        for obj in bpy.data.objects:
            if obj.type == "MESH":
                for mod in obj.modifiers:
                    if mod.type == "SUBSURF":
                        mod.levels = 0
                        mod.render_levels = 1
        steps.append("Minimal quality: subsurf disabled")
        bpy.context.scene.cycles.samples = 32
        steps.append("Samples reduced to 32")

    info["strategy"] = strategy
    info["steps_taken"] = steps
    return info


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    strategy = argv[0] if argv else "auto"

    result = apply_degrade_strategy(strategy)
    print(f"[OK] Degrade strategy '{strategy}' applied")
    for step in result.get("steps_taken", []):
        print(f"  - {step}")
