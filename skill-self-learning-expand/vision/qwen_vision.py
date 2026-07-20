
"""
Qwen-VL API 视觉分析工具
使用千问免费 API (DashScope / SiliconFlow)
用法:
  python qwen_vision.py caption <image_path>
  python qwen_vision.py analyze <image_path>
"""

import base64, json, sys, os
from pathlib import Path

# ========== 配置 ==========
# 填入你的 API Key:
DASHSCOPE_KEY = os.environ.get("DASHSCOPE_API_KEY", "sk-xxxxx")

# DashScope API (阿里云百炼)
API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
# 备用: SiliconFlow (https://siliconflow.cn)
# API_URL = "https://api.siliconflow.cn/v1/chat/completions"
# DASHSCOPE_KEY = os.environ.get("SILICONFLOW_API_KEY", "sk-xxxxx")

# ========== 模型选择 ==========
# 免费: qwen-vl-plus | qwen2-vl-7b-instruct (SiliconFlow)
MODEL = "qwen-vl-plus"
# ===========================

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def analyze_image(image_path, prompt="详细描述这张图片的内容"):
    if DASHSCOPE_KEY.startswith("sk-") and DASHSCOPE_KEY != "sk-xxxxx":
        key = DASHSCOPE_KEY
    else:
        print("[ERROR] 请在 qwen_vision.py 中填入你的 API Key")
        return None
    
    b64 = encode_image(image_path)
    
    import requests
    payload = {
        "model": MODEL,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
                {"type": "text", "text": prompt}
            ]
        }],
        "max_tokens": 500
    }
    
    resp = requests.post(API_URL, json=payload,
        headers={"Authorization": f"Bearer {key}"}, timeout=60)
    
    if resp.status_code == 200:
        return resp.json()["choices"][0]["message"]["content"]
    else:
        print(f"[ERROR] {resp.status_code}: {resp.text[:300]}")
        return None

def analyze_blender_render(image_path):
    """分析 Blender 渲染输出"""
    result = analyze_image(image_path, "Describe this 3D render in detail: what objects are there, materials, lighting setup, composition, and overall quality.")
    return result

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python qwen_vision.py caption <image_path>")
        print("       python qwen_vision.py analyze <image_path>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    path = sys.argv[2]
    
    if cmd == "caption":
        result = analyze_image(path, "用中文描述这张图片的主要内容")
    elif cmd == "analyze":
        result = analyze_blender_render(path)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
    
    if result:
        print(result)
