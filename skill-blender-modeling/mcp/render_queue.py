# Blender 批量渲染队列管理器
# 用法: python render_queue.py <scene.blend> --cameras cam1,cam2 --frames 1-120 --output ./renders/
# 或从分镜JSON读取: python render_queue.py <scene.blend> --storyboard shots.json

import json
import subprocess
import sys
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BRIDGE_DIR = Path(__file__).parent
BLENDER_BRIDGE = BRIDGE_DIR / "blender_bridge.py"

def load_storyboard(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def render_task(blend_file, frame, output_dir, camera=None):
    cmd = [
        sys.executable, str(BLENDER_BRIDGE), "render", blend_file,
        "--frame", str(frame),
        "--output", output_dir
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    return frame, result.returncode, result.stdout

def main():
    if len(sys.argv) < 3:
        print("Usage: python render_queue.py <scene.blend> [--cameras c1,c2] [--frames 1-120] [--storyboard shots.json] [--output ./renders/] [--parallel 2]")
        sys.exit(1)

    blend_file = sys.argv[1]
    cameras = []
    frame_range = (1, 1)
    output_dir = "./renders/"
    parallel = 2

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--cameras" and i+1 < len(sys.argv):
            cameras = [c.strip() for c in sys.argv[i+1].split(",")]
            i += 2
        elif sys.argv[i] == "--frames" and i+1 < len(sys.argv):
            parts = sys.argv[i+1].split("-")
            frame_range = (int(parts[0]), int(parts[1]))
            i += 2
        elif sys.argv[i] == "--storyboard" and i+1 < len(sys.argv):
            data = load_storyboard(sys.argv[i+1])
            cameras = [s.get("camera", "Camera") for s in data.get("shots", [])]
            frame_range = (data.get("start_frame", 1), data.get("end_frame", 120))
            output_dir = data.get("output", output_dir)
            i += 2
        elif sys.argv[i] == "--output" and i+1 < len(sys.argv):
            output_dir = sys.argv[i+1]
            i += 2
        elif sys.argv[i] == "--parallel" and i+1 < len(sys.argv):
            parallel = int(sys.argv[i+1])
            i += 2
        else:
            i += 1

    os.makedirs(output_dir, exist_ok=True)
    frames = list(range(frame_range[0], frame_range[1] + 1))

    total = len(frames) * max(len(cameras), 1)
    print(f"Render Queue: {total} tasks ({len(frames)} frames x {max(len(cameras), 1)} cameras)")
    print(f"Output: {os.path.abspath(output_dir)}")
    print(f"Parallel workers: {parallel}")
    print("-" * 50)

    completed = 0
    failed = 0

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {}
        for frame in frames:
            for cam in (cameras if cameras else [None]):
                futures[executor.submit(render_task, blend_file, frame, output_dir, cam)] = (frame, cam)

        for future in as_completed(futures):
            frame, cam = futures[future]
            try:
                f, code, stdout = future.result()
                if code == 0:
                    completed += 1
                    print(f"[{completed}/{total}] Frame {f} OK")
                else:
                    failed += 1
                    print(f"[FAIL] Frame {f}: {stdout[-200:]}")
            except Exception as e:
                failed += 1
                print(f"[FAIL] Frame {frame}: {e}")

    print("-" * 50)
    print(f"Done: {completed} OK, {failed} failed")

if __name__ == "__main__":
    main()
