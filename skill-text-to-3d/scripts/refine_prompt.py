"""
文字→三视图 → 3D 建模 — 描述润色脚本
"""
import sys, os, json, re
from pathlib import Path
from datetime import datetime

env_path = Path(__file__).parent.parent.parent.parent / "work/ai-start/.env"
if env_path.exists():
    for line in env_path.read_text(encoding="utf-8").strip().splitlines():
        k, v = line.split("=", 1)
        os.environ[k.strip()] = v.strip()

from openai import OpenAI
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com/v1")

def extract_json(text):
    # Try direct parse first
    text = text.strip()
    try:
        return json.loads(text)
    except:
        pass
    # Try extracting from markdown code block
    m = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text)
    if m:
        try:
            return json.loads(m.group(1))
        except:
            pass
    # Try finding first { and last }
    start = text.find('{')
    end = text.rfind('}')
    if start >= 0 and end > start:
        try:
            return json.loads(text[start:end+1])
        except:
            pass
    raise ValueError("No valid JSON found in response")

if __name__ == "__main__":
    desc = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("描述：")
    print(f"\n原始描述: {desc}\n{'='*50}")
    
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你只输出JSON，不输出任何其他文字。JSON必须包含这些字段：object(物件名), style(风格), three_views(含front正面/side侧面/top俯视), tone(色调说明), style_recommendation(推荐的通义万相风格)"},
            {"role": "user", "content": f"把「{desc}」这个物件设计成三视图JSON"}
        ],
        stream=False
    )
    
    raw = resp.choices[0].message.content
    result = extract_json(raw)
    
    views = result.get("three_views", {})
    print(f"\n物件: {result.get('object','?')}")
    print(f"风格: {result.get('style','?')}")
    print(f"\n三视图:")
    for vk, vl in [("front","正面"),("side","侧面"),("top","俯视")]:
        print(f"  {vl}: {views.get(vk,'?')}")
    print(f"\n推荐风格: {result.get('style_recommendation','-')}")
    
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    op = Path(__file__).parent.parent / "references" / f"prompt_{ts}.json"
    Path(op).write_text(json.dumps({"raw": desc, "refined": result}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n已保存: {op}")
