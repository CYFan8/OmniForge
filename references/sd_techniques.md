# SD 1.5 高质量出图技巧

## Prompt 工程

### 质量前缀（必须放最前面）
masterpiece, best quality, 8k, highly detailed, intricate, sharp focus, professional

### 风格关键词
photorealistic / cinematic lighting / volumetric fog / god rays / depth of field / bokeh / national geographic style

### 负面 Prompt（SD 1.5 专用）
worst quality, low quality, normal quality,
bad anatomy, bad hands, missing fingers, extra fingers,
blurry, jpeg artifacts, signature, watermark, text, username,
ugly, deformed, distorted, disfigured,
poorly drawn, bad proportions, extra limbs, cloned face,
grainy, noisy, oversaturated, bad composition,
mutation, deformed, fused fingers, too many fingers,
long neck, cropped, out of frame

## 最佳参数

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| CFG Scale | 7-9 | 太低模糊，太高过饱和 |
| Steps | 30-50 | 30=速度优先，50=质量优先 |
| Resolution | 512x768 | SD 1.5 原生分辨率，竖构图效果好 |
| Sampler | DDIM / Euler | 快速稳定 |
| Seed | -1 (随机) | 跑多次挑最好的 |
| Batch | 1-2 | 单张质量最好 |

## 主题 prompt 模板

### 人物
masterpiece, best quality, 8k, portrait of [描述], [服装], [表情], [光线], [背景], detailed face, detailed eyes, photorealistic

### 场景
masterpiece, best quality, 8k, cinematic wide shot of [场景], [天气], [时间], [氛围], volumetric lighting, depth of field, highly detailed environment

### 科幻/赛博朋克
masterpiece, best quality, 8k, cyberpunk [场景], neon lights, holographic, rain-slicked streets, [色调], cinematic composition, blade runner style

## 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| 画面模糊 | CFG 太低 / steps 太少 | CFG 7-9, steps 30+ |
| 人物变形 | negative prompt 不够 | 加 bad anatomy, extra limbs |
| 色彩过饱和 | CFG 太高 | 降到 7-8 |
| 噪点 | steps 太少 | 30-50 steps |
| 构图差 | 没指定构图词 | 加 cinematic composition, wide shot |

## 实测对比 (RTX 4060)

| 配置 | 耗时 | 质量 |
|------|------|------|
| 简单 prompt + 20 steps | 5.4s | 一般 |
| 增强 prompt + 40 steps + 专业 neg | 14.5s | 优秀 |
| 增强 prompt + 50 steps | ~18s | 最佳 |
