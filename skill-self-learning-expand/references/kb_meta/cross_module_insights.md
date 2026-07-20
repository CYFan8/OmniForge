# 跨模块学习洞察

> 来源: JOURNEY.md (23个踩坑) + CHANGELOG.md + 全模块SKILL.md
> 学习轮次: 第2轮 (2026-07-20)

## 从项目历史学到的跨模块教训

### 环境与部署 (全模块通用)
| 教训 | 来源 | 适用模块 |
|------|------|---------|
| 不创建venv: Codex runtime自带CUDA torch | JOURNEY Phase 4 | 生图/建模 |
| 先查runtime有什么: 绕了3小时才发现CUDA已就绪 | JOURNEY Phase 3 | 全模块 |
| PCL百宝箱是万能下载器: 墙内大文件首选 | JOURNEY Phase 3 | 全模块 |
| PowerShell+UTF-8+中文=编码地狱: 纯英文注释最安全 | JOURNEY Phase 4 | 全模块 |
| 破解版PS没有COM: 正版≠破解版 | JOURNEY Phase 6 | 生图 |

### 架构设计 (全模块通用)
| 教训 | 来源 | 适用模块 |
|------|------|---------|
| 文档驱动Skill必须逐条对齐大纲: 不能自作主张合并 | JOURNEY Phase 1 | 全模块 |
| SAI文件系统桥接是最稳健的: 无需服务, 始终可用 | JOURNEY 教训6 | 生图/建模 |
| MCP桥接架构: 检测→分发→回退, 保留兜底链路 | JOURNEY Phase 2 | 全模块 |

### 生图模块专属
| 教训 | 细节 |
|------|------|
| SD模型下载地狱 | GitHub/AUTOMATIC1111被墙→放弃GUI, 自建轻量FastAPI服务 |
| torch版本陷阱 | 清华镜像只有CPU版→直接用runtime Python |
| HF Hub超时 | 设HF_ENDPOINT=https://hf-mirror.com |
| GPU性能 | RTX 4060: 512x512/25steps=8.3s (CPU同配135s, 16倍加速) |

### 建模模块专属 (新增, 从本轮学习提取)
| 教训 | 细节 |
|------|------|
| bpy必须进程内运行 | Blender Python API无法外部导入, 必须 `blender --background --python` |
| Steam版Blender路径 | 不在常规Program Files, 在F:\steam\steamapps\common\ |
| 后台渲染需显式设CUDA | 否则Cycles回退到CPU |
| JSON BOM问题 | PowerShell的Out-File默认加BOM, Python json.load不兼容 |

## 跨模块知识复用矩阵

### 剧本 → 生图
- 分镜描述可转为SD提示词: 场景描述 + 人物外貌 -> prompt
- 氛围关键词对应SD光影关键词: "安静疏离" -> "soft diffused light, moody"

### 生图 → 建模
- 角色概念图 -> 三视图 -> Blender体块建模
- SD输出分辨率需与Blender渲染一致 -> 1920x1080
- PBR材质参数速查表 -> Blender Principled BSDF节点

### 建模 → 生图
- 三渲二线稿 -> SD img2img叠加材质
- 灰度底图 -> ControlNet Canny锁结构 -> SD风格化
- Denoising 0.35保结构, CFG 7-8.5保自然

### 全模块 → 自主学习
- 各模块SKILL.md -> 注册学习子Skill
- 缺陷记录 -> 回写各模块references/
- 用户反馈 -> 动态调整评分权重
