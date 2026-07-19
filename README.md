# OmniForge

> *Forge every skill. Approach omniscience.*
> 趋近全能的 AI 技能共同体。四层架构，开源共建。

---

## 这是什么

OmniForge 不是 Prompt 合集。是一套**可部署、可扩展、社区共建的 AI 创作引擎**。

它把 AI 能力拆成四层——从全局配置到核心调度、从剧本创作到 GPU 生图、从模型评分到知识库检索——每一层都可以独立使用，也可以串联成完整工作流。

## 为什么做这个

现在的 AI 工具碎片化严重：写剧本用一个、生图用另一个、评分还得手动。每次切换工具都在消耗创造力。

OmniForge 把这一切焊在一起：

- **一个人用**：安装即用，写剧本 → 出分镜 → GPU 生图，全链路打通
- **团队用**：共享 Skill 文件，统一 prompt 规范和质量标准
- **社区用**：任何人可以贡献新 Skill，Fork → 写 SKILL.md → PR 合并

**目标很朴素**：让 AI 创作从「能用」变成「好用」，从「一个人的工具」变成「一群人的生态」。

## 架构

```
Layer 1: 全局设置     AGENTS.md + system-global-settings
         ↓           启动配置 · 模组隔离 · RAG分区 · 评分阈值
Layer 2: 核心技能     17 项底层调度（后台静默运行）
         ↓           开机自检 · Agent调度 · Token管控 · 日志系统
Layer 3: 业务拓展     剧本创作(13项) + GPU生图(16项) + MCP桥接
         ↓           世界观归档 · 冲突校验 · 双引擎生图 · 像素校验
Layer 4: 模型评分     裸分+综合分双层打分 · 低分兜底 · 智能推荐
```

## 快速开始

```bash
git clone https://github.com/CYFan8/OmniForge.git
```

### 生图引擎
```bash
# 安装依赖
pip install diffusers transformers accelerate fastapi uvicorn safetensors torch

# 下载模型（从 hf-mirror）
set HF_ENDPOINT=https://hf-mirror.com
python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='XpucT/Deliberate', filename='Deliberate_v2.safetensors', cache_dir='./models')"

# 启动 GPU Server (:7861)
set PATH={python_runtime}/DLLs;{python_runtime};%PATH%
python sd_mcp_gpu_server.py

# 生图
curl -X POST http://127.0.0.1:7861/mcp/sdapi/v1/txt2img \
  -H "Content-Type: application/json" \
  -d '{"prompt":"masterpiece, best quality, a lone samurai in cyberpunk city","steps":35}'
```

## 技能总览

| 技能 | 条目 | 说明 |
|------|------|------|
| system-global-settings | 4 分区 | 全局配置面板 |
| skill-system-core | 17 项 | 底层核心调度 |
| skill-script-creation | 13 项 | 剧本创作引擎 |
| skill-image-generation | 16 项 + MCP | GPU生图引擎 |
| skill-model-scoring | 5 项 | 模型评分机制 |

## 实测性能

| 引擎 | 模型 | 分辨率 | 耗时 |
|------|------|--------|------|
| GPU | SD 1.5 | 512x768 | 8.3s |
| GPU | Deliberate v2 | 512x768 | 11-15s |
| CPU | SD 1.5 | 512x512 | 135s |

## 共建指南

```bash
# 1. Fork 本仓库
# 2. 创建你的技能目录: skill-你的技能名/
# 3. 写 SKILL.md（参考 skill-system-core/SKILL.md 格式）
# 4. 提交 PR，描述你的技能解决了什么问题
```

每个 Skill 只需要一个 SKILL.md 文件。参考现有任意一份即可。

## 踩坑实录

部署过程中遇到了 23 个实机问题——从 GitHub 被墙到 Python venv 丢失 ctypes 到破解版 PS COM 不可用。每个都记录了根因和解决方案，分散在各 SKILL.md 的「踩坑实录」章节和 [JOURNEY.md](JOURNEY.md) 中。

## 许可

MIT — 拿去用，改，分发。只希望你觉得有用时也贡献回来。

---

**CYFan8 · 2026**
