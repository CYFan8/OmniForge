---
name: skill-image-generation
description: >-
  生图联动专属拓展包。当用户需要生成图像、进行剧本联动分镜绘图、
  高清图像多轮解析、Photoshop/Stable Diffusion双绘图链路切换、
  像素级闭环自动校验、批量连贯出图时激活。仅承载图像生成业务，
  独立运行状态下不主动读取剧本模组任何文本数据。
  内置 MCP 桥接支持 Photoshop COM / Stable Diffusion API / SAI Filesystem / Krita API。
---

# 生图联动专属拓展包（16项）

## 1. 分镜预解析
拆解剧本文本生成分层绘图提示词。解析剧本模组推送的分镜文本，自动拆分场景、人物、镜头细节，生成分层精细化标准化绘图提示词。

## 2. 角色锁定
统一人物五官服饰避免画面崩坏。自动调取RAG图像分区人物向量数据，锁定角色五官、体型、服饰特征，保障连续分镜人物形象统一。

## 3. 画风模板
提供国风、写实、二次元、电影质感四种渲染风格。内置写实、电影质感、二次元、国风四套全局画风模板，支持用户自由切换选用。

## 4. 图像解析
放大参考图提取配色人物细节参数。搭载独立图像识别底层工具，支持图片局部裁切放大解析人设参考图、道具图纸、建筑三视图细节。Agent多轮迭代优化图像文字描述。

## 5. 三视图重建
根据图纸生成完整彩色效果图。上传道具、建筑三视图图纸，自动生成完整彩色概念效果图。

## 6. PS调度（MCP Photoshop COM Bridge）
调用专业绘图软件分层画布渲染。通过 MCP Photoshop Bridge（`mcp/photoshop_bridge.py`）COM自动化连接 Photoshop，启用内置 Firefly AI 绘图能力。支持分层画布创建、选区局部重绘、画面横纵向扩图、细节修补。批量生成成套人设卡、连贯分镜、场景概念图，自动按剧本分镜分类归档，支持多尺寸画布批量导出。

**MCP 连接**:
```
python mcp/router.py generate ps "prompt text" --width 1920 --height 1080
```

## 7. SD调度（MCP Stable Diffusion REST Bridge）
无PS时启用开源绘图引擎运行。通过 MCP SD Bridge（`mcp/sd_bridge.py`）连接 Stable Diffusion WebUI API。完整保留图像校验、批量生成、细节优化全部基础绘图功能。

**MCP 连接**:
```
python mcp/router.py generate sd "prompt text"
```

## 8. 引擎切换
根据环境自动选用合适绘图工具。通过 MCP Router（`mcp/router.py`）自动检测可用工具并按优先级路由：SD API > Photoshop COM > Krita > SAI。路由配置见 `mcp/config.json`。

## 9. 像素校验
对比原图，量化画面细节差异程度。调用底层pixelmatch像素比对工具，量化计算生成图与用户参考图像素差值，支持自定义像素差异合格阈值。

## 10. 局部重绘
针对缺陷区域单独优化修正画面。画面未达标时自动优化提示词、针对缺陷区域局部重绘。智能区分轻微渲染噪点与人物五官服饰实质性画面缺陷，执行差异化修复逻辑。

**MCP 重绘**:
```
python mcp/router.py refine sd <input_image> "fix the eyes and add more detail"
```

## 11. 色调绑定
统一整套分镜光影色彩氛围。提取指定参考图专属配色体系，统一全部生成画面色温、饱和度、明暗对比度。

## 12. 批量绘图
一次性生成整本剧本全部画面。统一全套分镜光影强度、色调倾向、镜头透视参数，保障整套画面视觉风格一致性。

## 13. CLIP校验
核对画面与文字描述是否匹配。核对生成画面内容与文本提示词匹配度，画面缺失关键场景、道具、人物特征时自动触发二次重绘。

## 14. 素材归档
分类存储生成图片与参考资源。持久存储AI生成原画、用户上传参考素材，按剧本、人物、场景分类存储，支持随时检索复用。

## 15. 高负载降级
算力不足关闭高精度渲染功能。任务运行出现推理算力紧张、Token触及配额上限、图像迭代重绘达到轮次上限时，自动关闭高精度像素比对校验，切换低成本文字语义匹配模式。

## 16. 联动接口
接收剧本传输的人设分镜数据。仅联动通道开启后激活，解析剧本模组推送的分镜文本、完整人设参数、场景光影氛围描述。

---

## MCP 桥接架构

```
skill-image-generation/mcp/
├── config.json          # 桥接配置（工具列表、路由优先级、依赖）
├── router.py            # 统一路由器（检测、分发、回退）
├── photoshop_bridge.py  # Photoshop COM 自动化桥接
├── sd_bridge.py          # Stable Diffusion REST API 桥接
├── sai_bridge.py         # SAI 文件系统桥接
├── krita_bridge.py       # Krita Python API 桥接（待实现）
└── init.ps1              # 一键初始化脚本
```

### 路由优先级（auto_fallback=true）
1. Stable Diffusion API（首选：全自动生图）
2. Photoshop COM（次选：Firefly AI + 分层编辑）
3. Krita API（备选：开源数字绘画）
4. SAI Filesystem（兜底：文件系统中转）

### MCP 命令速查
```bash
# 初始化所有桥接
python mcp/router.py init

# 查看所有工具状态
python mcp/router.py status

# 生图（自动选择最佳工具）
python mcp/router.py generate sd "a cyberpunk city at night, neon lights"

# 用 Photoshop 创建画布
python mcp/router.py generate ps "character design" --width 1920 --height 1080

# 精细修复已有图片
python mcp/router.py refine sd ./input.png "make lighting warmer, add fog"

# SAI 工作流
python mcp/router.py generate sai "draw a warrior character"
```

---

## 依赖清单

### MCP 桥接依赖
| 组件 | 用途 | 安装命令 |
|------|------|---------|
| pywin32 | Photoshop COM 自动化 | `pip install pywin32` |
| requests | SD API HTTP 请求 | `pip install requests` |
| Pillow | 图像格式处理 | `pip install Pillow` |
| watchdog | SAI 文件监控（可选） | `pip install watchdog` |

### 绘图引擎
| 软件 | 用途 | 获取方式 |
|------|------|---------|
| Photoshop CC 2021+ (+ Firefly) | 专业分层AI绘图 | Adobe官网订阅 |
| Stable Diffusion WebUI | 开源AI绘图引擎 | `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui` |
| PaintTool SAI / SAI2 | 日系数字绘画 | SYSTEMAX官网 |
| Krita 5.0+ | 开源数字绘画 | krita.org 免费下载 |

### 一键初始化
```powershell
# 安装依赖 + 检测所有工具
powershell -ExecutionPolicy Bypass -File D:\ai_skill_lib\skill-image-generation\mcp\init.ps1
```

---

## 规则联动

- 绘图链路选择 → 受 MCP Router 自动检测与路由
- 模组隔离 → 受 system-global-settings 隔离规则约束
- Token管控 → 联动 skill-system-core 弹性Token管控
- 像素校验(9) → 调用底层pixelmatch工具
- 降级兜底(15) → 联动 skill-system-core 低分兜底
- 联动接口(16) → 接收 skill-script-creation 单向推送
- MCP 状态 → 写入 skill-system-core 日志系统

---

## 实测数据

### 双引擎对比

| 引擎 | 硬件 | 精度 | 步数 | 分辨率 | 耗时 | 状态 |
|------|------|------|------|--------|------|------|
| SD 1.5 GPU | RTX 4060 Laptop | fp16 | 25 | 512x512 | 8.3s | 生产就绪 |
| SD 1.5 CPU | Intel i7 | fp32 | 20 | 512x512 | 135s | 可用 |
| Photoshop 2023 | 破解版 | - | - | - | - | COM 不可用 |
| SAI 文件桥接 | 手动 | - | - | - | - | 提示词就绪 |

### 部署经验

- 不要创建 venv: Codex runtime Python 自带 CUDA torch，创建隔离环境反而引发 DLL 路径冲突
- HF Hub 被墙: 模型配置文件走 hf-mirror.com 镜像
- PyTorch CDN 被墙: 用户通过 PCL 百宝箱下载 CUDA torch wheel
- 破解版 PS: COM 注册不完整，桥接不可用；正版 PS 可通过 photoshop_bridge.py 连接
- SAI: 不需要任何运行服务，文件系统桥接始终可用

### 环境要求

SD GPU 模式需满足：
1. Codex runtime Python（自带 CUDA torch 2.6.0+cu124）
2. SD 1.5 safetensors 模型文件（4GB，从 hf-mirror.com 下载）
3. NVIDIA GPU + 4GB VRAM（RTX 4060 测试通过）
4. HF_ENDPOINT=https://hf-mirror.com（首次加载需下载 pipeline 配置）

---

## 提示词工程

> 技巧来源: 实测验证 (2026-07-19)
> 完整技巧库: D:\ai_skill_lib\references\sd_techniques.md

### 质量前缀模板

```
masterpiece, best quality, 8k, highly detailed, intricate, sharp focus, professional, [主题], [风格], [光线], [构图]
```

### 标准负面 Prompt

```
worst quality, low quality, bad anatomy, bad hands, extra fingers, blurry, jpeg artifacts, signature, watermark, ugly, deformed, distorted, disfigured, poorly drawn, bad proportions, extra limbs
```

### 推荐参数

| 参数 | 基础 | 推荐 | 极致 |
|------|------|------|------|
| Steps | 20 | 30-40 | 50 |
| CFG | 7 | 7-8.5 | 9 |
| 分辨率 | 512x512 | 512x768 | 768x768 |
| 耗时(RTX 4060) | ~5s | ~14s | ~20s |

### 质量对比

| 配置 | 耗时 | 效果 |
|------|------|------|
| 简单 prompt, 20 steps | 5.4s | 一般 |
| 增强 prompt + 专业 neg, 40 steps | 14.5s | 优秀 |


---

## AI 生图完整技巧 (更新 2026-07-19)

> 手册: D:\\ai_skill_lib\\references\\ai_image_techniques.md

### 二次元
- 风格锚点: studio ghibli / makoto shinkai / kyoani / cyberpunk anime
- 核心词: cel shaded, 2d art, flat color, clean lines
- CFG 9-12 | Steps 35-50
- 负面排除: 3d, realistic, photorealistic

### 写实
- 光线: golden hour / volumetric lighting / studio lighting
- CFG 7-8.5 | Steps 30-45
- photography, national geographic style

### Prompt 黄金法则
1. 质量词 > 2. 风格锚点 > 3. 主体 > 4. 细节 > 5. 画师
单元素: a single, solo, clean background + 负面排除 crowd, group

---

## 踩坑实录与解决方案

> 以下均在 2026-07-19 实机部署中遇到并解决。

### 模型下载

| 问题 | 现象 | 解决 |
|------|------|------|
| Git clone AUTOMATIC1111 SD WebUI 失败 | GitHub / gitclone / ghproxy / Gitee 全部超时 | 放弃 SD WebUI GUI；直接用 diffusers 库 + FastAPI 自建轻量服务端 |
| HuggingFace 模型下载超时 | `ConnectTimeout / ReadTimeout` | 设 `HF_ENDPOINT=https://hf-mirror.com` + 用 `huggingface_hub.hf_hub_download()` |
| hf-mirror 大文件 404 | `anything-v5.safetensors: 404` | 换可达的模型 repo（如 `XpucT/Deliberate`） |
| curl 从镜像下载 2GB 需 15 分钟 | 400KB/s 持续波动 | 正常，等。或 PCL 百宝箱自定义下载可能更快 |

### 生图质量

| 问题 | 现象 | 解决 |
|------|------|------|
| 画面模糊/细节丢失 | 简单 prompt + 20 steps | 加质量前缀 `masterpiece, best quality, 8k` + 40+ steps |
| 人物手指畸形 | 缺负面 prompt | 负面加 `bad hands, extra fingers, fused fingers, bad anatomy` |
| 二次元像 3D 渲染 | SD 1.5 是写实模型 | 换 Deliberate v2 + CFG 9-12 + 风格锚点 `anime style, cel shaded` |
| 写实像动画/插画 | CFG 太高 | CFG 降到 7-8 + `photorealistic, photograph, national geographic` |
| 动物多条腿/畸形 | 缺反向约束 | 正面加 `quadruped, four legs`；负面排除 `extra legs, six legs, multiple limbs` |

### 双引擎切换

| 问题 | 现象 | 解决 |
|------|------|------|
| PS COM 不可用（破解版） | `pywintypes.com_error: 没有注册类` | 破解版 PS 2023 无 COM 无 Firefly。正版 PS 2024+ 可通过 `photoshop_bridge.py` 连接 |
| SAI 无 API | 需手动操作 | `sai_bridge.py` 用文件系统中转：写提示词 → 用户手绘 → 自动收集。无需运行服务 |
| SD Server 端口被占 | `[Errno 10048]` | 杀掉旧进程 `taskkill /f /im python.exe` 后重启 |
| Server 启动后模型加载卡住 | 无输出，端口不可达 | 首次加载需 30-60 秒（CPU）或 10-20 秒（GPU），等 |

### 已废弃方案

| 方案 | 废弃原因 |
|------|---------|
| 创建独立 venv | 引发 DLL 路径冲突、ctypes 丢失 |
| 设置 PYTHONHOME | 导致 stdlib encodings 丢失 |
| AUTOMATIC1111 SD WebUI | git clone 所有源均超时 |
| 清华镜像 pip install torch | 只提供 CPU 版 `2.13.0+cpu`，无 CUDA |
| 官方 PyTorch CDN | `download.pytorch.org` 被墙 ReadTimeout |
