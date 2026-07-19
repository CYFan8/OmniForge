## 四层架构系统 — 开发历程

### 时间线

#### Phase 1: 架构落地 (约 2 小时)
- 基于完整四层架构精密文档，在 D:\ai_skill_lib\ 创建 5 个核心 Skill
- **踩坑**: 初期犯了"过度合并"的错误，把 17 项核心技能压缩成 6 个文件
- **修复**: 用户要求严格对齐大纲后，删掉合并版，改为 1 个 skill-system-core 承载全部 17 项，每个 H2 对应一条
- **教训**: 文档驱动的 Skill 必须逐条对齐用户大纲，不能自作主张合并

#### Phase 2: MCP 桥接架构
- 创建 skill-image-generation/mcp/ 下 5 个脚本 + 配置
- **photoshop_bridge.py**: Windows COM 自动化（后续发现破解版不可用）
- **sd_bridge.py**: Stable Diffusion REST API 桥接
- **sai_bridge.py**: 文件系统桥接（无需运行服务，始终可用）
- **router.py**: 统一路由器（检测 → 分发 → 回退）
- **config.json**: 桥接配置 + 路由优先级

#### Phase 3: SD 部署 — 地狱模式 (约 4 小时)
| 尝试 | 方法 | 结果 |
|------|------|------|
| 1 | git clone GitHub AUTOMATIC1111 | 被墙，Connection reset |
| 2 | git clone gitclone.com 镜像 | 超时 |
| 3 | git clone ghproxy.com 代理 | 超时 |
| 4 | git clone Gitee 镜像 | 超时 |
| 5 | pip install diffusers (清华镜像) | 成功装包，但 torch 是 CPU 版 |
| 6 | pip install torch --index-url pytorch.org | 2.5GB 下载被墙，ReadTimeout |
| 7 | 用户用 PCL 百宝箱下载 CUDA torch wheel | 成功，2.3GB 到位 |
| **8** | **发现 Codex runtime Python 自带 CUDA torch 2.6.0+cu124** | **终极方案！** |

#### Phase 4: Python 环境地狱
| 问题 | 原因 | 解决 |
|------|------|------|
| ModuleNotFoundError: ctypes | venv 隔离时把 stdlib DLLs 路径也删了 | 最小化修复：只 insert venv site-packages，保留所有 stdlib |
| CUDA not available | 清华镜像的 torch 是 CPU 版 (2.13.0+cpu) | 直接用 runtime Python，绕过 venv |
| 中文注释 SyntaxError | PowerShell 写入文件时 GBK 编码破坏 UTF-8 | 改用 Node REPL 写文件，纯英文注释 |
| Start-Process 不传环境变量 | Codex shell 隔离策略 | 写 .bat 文件让用户双击运行 |
| HF Hub 超时 | 模型配置文件需要从 huggingface.co 下载 | 设 HF_ENDPOINT=https://hf-mirror.com |

#### Phase 5: GPU 起飞
- **最终方案**: Codex runtime Python (C:\Users\l's'y\.cache\codex-runtimes\...\python\python.exe)
- **模型**: runwayml/stable-diffusion-v1-5, 用户从 hf-mirror 下载 safetensors 文件
- **硬件**: NVIDIA RTX 4060 Laptop GPU (4GB VRAM), fp16, attention_slicing
- **性能**: 512x512 / 25 steps = **8.3 秒/张** (CPU 同配置 135 秒，16 倍加速)

#### Phase 6: Photoshop 桥接尝试
- PS 2023 安装在 D:\GZ\Adobe Photoshop 2023\
- COM ProgID 存在于注册表 (Photoshop.Application.170) 但无法初始化
- **根因**: 破解版跳过了 COM 服务器注册 (pywintypes.com_error: 没有注册类)
- **现状**: PS 自动化不可用，保留桥接代码供正版用户使用

---

### 关键教训

1. **不要创建 venv**: Codex runtime 的 Python 已经是完整环境，创建 venv 会引入路径冲突
2. **先查 runtime 有什么**: 我们绕了 3 小时才发现 runtime 自带 CUDA torch
3. **中文注释是定时炸弹**: PowerShell + UTF-8 + 中文字符 = 编码地狱，纯英文最安全
4. **PCL 是万能下载器**: 墙内下载大文件，PCL 百宝箱比任何镜像都好用
5. **破解版 PS 没有 COM**: 正版 Adobe 的 COM 自动化 ≠ 破解版的
6. **SAI 文件系统桥接是最稳健的**: 不需要任何运行服务，始终可用

---

### 当前工作状态

| 组件 | 状态 | 端口 | 性能 |
|------|------|------|------|
| SD GPU Server | ✅ 运行中 | 7861 | 8.3s/张 |
| PS COM Bridge | ❌ 破解版不可用 | — | — |
| SAI Filesystem Bridge | ✅ 就绪 | — | 手动 |
| MCP Router | ✅ 就绪 | — | — |
| system-global-settings | ✅ 4 分区配置完整 | — | — |
| skill-system-core | ✅ 17 项完整 | — | — |
| skill-script-creation | ✅ 13 项完整 | — | — |
| skill-image-generation | ✅ 16 项 + MCP | — | — |
| skill-model-scoring | ✅ 5 项完整 | — | — |

### 启动命令速查

```bash
# GPU 生图 Server
set PATH=C:\Users\l's'y\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\DLLs;...;%PATH%
set HF_ENDPOINT=https://hf-mirror.com
python D:\sd-webui\sd_mcp_gpu_server.py

# MCP 路由
python D:\ai_skill_lib\skill-image-generation\mcp\router.py init
python D:\ai_skill_lib\skill-image-generation\mcp\router.py generate sd "your prompt"

# SAI 工作流
python D:\ai_skill_lib\skill-image-generation\mcp\router.py generate sai "your prompt"
```
