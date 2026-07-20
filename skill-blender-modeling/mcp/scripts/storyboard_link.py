"""
建模能力 9: 分镜联动
接收剧本模块的分镜数据, 自动搭建场景Layout
"""

import bpy
import sys
import json


def parse_storyboard(json_path):
    """从JSON文件读取分镜数据"""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def layout_from_storyboard(storyboard_data):
    """根据分镜数据搭建场景Layout"""
    scenes = storyboard_data.get("scenes", [])
    for i, scene in enumerate(scenes):
        container_name = f"Scene_{i:03d}"
        bpy.ops.object.empty_add(type="PLAIN_AXES", location=(i * 5, 0, 0))
        container = bpy.context.active_object
        container.name = container_name

        desc = scene.get("description", "")
        print(f"[OK] Layout: {container_name} -> {desc[:60]}")

    print(f"[OK] Storyboard layout: {len(scenes)} scenes")


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    if argv and argv[0] == "layout" and len(argv) > 1:
        data = parse_storyboard(argv[1])
        layout_from_storyboard(data)
