---
name: skill-text-to-3d
description: "文字描述 → 三视图生成 → 3D建模 完整工作流。用户提供文字描述，经 DeepSeek 润色后用通义万相生成三视图，确认后在混元3D 生成模型。"
---

# 文字→三视图→3D 建模工作流

## 触发条件

用户想要把一段文字描述变成 3D 模型，关键词如：
- 「把这个做成 3D」
- 「帮我建模」
- 「我想做 XXX 的 3D 模型」
- 「文字→三视图→建模」

## 工作流概述

```
用户描述 → ① DeepSeek 润色细化 → ② 通义万相生成三视图
    → ③ 给用户确认 → ④ 混元3D 生成模型
```

## 第一步：描述润色（DeepSeek API）

调 DeepSeek 把用户的原始描述精细化，输出结构化的三视图提示词：

**示例输入**: 「一个复古台灯」

**示例输出**:
```json
{
  "object": "复古台灯",
  "style": "工业复古风，黄铜+墨绿色玻璃灯罩",
  "three_views": {
    "front": "正面视图：圆形底座直径15cm，黄铜灯杆高30cm，墨绿色玻璃灯罩呈倒梯形，顶部带金色旋钮",
    "side": "侧视图：灯杆中部有弧形开关拨杆，灯罩与灯杆连接处有螺纹接口",
    "top": "俯视图：圆形灯罩口径10cm，可见内部灯泡插座为E27标准螺口"
  },
  "tone": "写实产品渲染风格，白色背景，柔和环境光",
  "style_recommendation": "黏土拟物风 / 皮克斯风"
}
```

执行:
```bash
D:\work\ai-start\venv\Scripts\python.exe D:\ai_skill_lib\skill-text-to-3d\scripts\refine_prompt.py "用户描述"
```

## 第二步：用通义万相生成三视图

1. 浏览器已登录通义万相: [https://tongyi.aliyun.com/wan/explore](https://tongyi.aliyun.com/wan/explore)
2. 点击「图文生成」进入图文创作模式
3. 将 DeepSeek 输出的三视图描述填入文本框
4. 选择合适的风格（皮克斯风/黏土拟物风等）
5. 生成并截图给用户看

## 第三步：用户确认

- 如果满意 → 进入第四步
- 如果不满意 → 回到第一步调整描述

## 第四步：混元3D 生成

1. 用户确认三视图后，将精细化的描述复制
2. 打开腾讯混元3D: [https://3d-models.hunyuan.tencent.com/](https://3d-models.hunyuan.tencent.com/)
3. 粘贴描述，选择文本生成 3D
4. 下载生成的 OBJ/GLB 模型文件
5. 保存到 D:\3d-models\ 目录

## 注意事项

- 通义万相需要已登录状态（当前已登录）
- 混元3D 每日 10 次免费
- 三视图生成失败时可尝试换个风格或简化描述
- 最终模型文件格式优先使用 GLB（通用性好）