# OmniForge

> *Forge every skill. Approach omniscience.*
> 趋近全能的 AI 技能共同体 — 四层架构，开源共建。

<p align="center">
 <img src="https://img.shields.io/badge/version-v2.1-blue" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
 <img src="https://img.shields.io/badge/skills-5%20core%20%2B%204%20extensions%20%2B%20Qwen-orange" alt="skills">
 <img src="https://img.shields.io/badge/GPU-RTX%204060-brightgreen" alt="GPU">
 <img src="https://img.shields.io/badge/Browser-Playwright%201228-blueviolet" alt="playwright">
</p>

---

## 这是什么

OmniForge 不是 Prompt 合集。是一套**可部署、可扩展、社区共建的 AI 创作引擎**。

把 AI 能力拆成四层——从全局配置到核心调度、从剧本创作到 GPU 生图、从模型评分到知识库检索——每一层独立可用，也可以串联成完整工作流。

---

## 为什么做这个

AI 工具碎片化太严重了。写剧本用一个，生图用另一个，评分还得靠肉眼。每次切换都在消耗创造力。

OmniForge 要解决的只有一件事：**把散落的 AI 能力焊成一把趁手的工具**。

它不是某个特定 Prompt 的复制粘贴，而是一个技能框架——任何人都能基于它扩展自己的 AI 技能，像给瑞士军刀加配件一样。

---

## 架构

```
┌─────────────────────────────────────────────────────────────┐
│  L1  全局设置 (AGENTS.md + system-global-settings)          │
│      启动配置 · 模组隔离 · RAG 分区 · 评分阈值                │
├─────────────────────────────────────────────────────────────┤
│  L2  核心技能包 (skill-system-core)                          │
│      17 项底层调度：自检 · Agent调度 · Token管控 · 日志       │
├─────────────────────────────────────────────────────────────┤
 │  L3  业务拓展模组                                            │
 │      剧本创作(13) · GPU生图(16+MCP) · Blender建模(14+MCP)   │
 │      自主学习(8+扩容+视觉引擎)                                │
 ├─────────────────────────────────────────────────────────────┤
 │  L4  模型评分 (skill-model-scoring) + 千问Qwen生图/视觉管线   │
│      裸分+综合分 · 低分兜底 · 智能推荐                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 技能清单

### 🟢 system-global-settings — 全局设置面板

**4 个配置分区**：启动配置 · 模组隔离 · RAG 知识库 · 评分阈值

所有模块的运行逻辑强制受此约束。每次启动自动加载，是整个系统的「开关总闸」。

### 🟢 skill-system-core — 17 项核心技能

后台静默运行的基础能力层，用户看不到但缺了哪个都崩：

| # | 技能 | # | 技能 |
|---|------|---|------|
| 1 | 开机自检 | 10 | 弹性 Token 管控 |
| 2 | 绘图软件分发 | 11 | 低分兜底处置 |
| 3 | 文档解析 | 12 | 全链路日志 |
| 4 | RAG 向量底座 | 13 | 素材导入导出 |
| 5 | 双层记忆 | 14 | 外网限流重试 |
| 6 | 工具自动更新 | 15 | 模型切换适配 |
| 7 | Agent 调度中枢 | 16 | GitHub 仓库检索 |
| 8 | 上下文压缩 | 17 | 技能归属判定 |
| 9 | 模组互联锁 | | |

### 🟢 skill-script-creation — 剧本创作 (13 项)

| # | 功能 | # | 功能 |
|---|------|---|------|
| 1 | 世界观归档 | 8 | 剧本格式化 |
| 2 | 设定冲突校验 | 9 | 批量导出 |
| 3 | RAG 剧情检索 | 10 | 分镜生成 |
| 4 | 台词风格校准 | 11 | 跨包数据推送 |
| 5 | 多分支推演 | 12 | 时间线纠错 |
| 6 | 冲突节奏分析 | 13 | 道具一致性 |
| 7 | 伏笔梳理 | | |

### 🟢 skill-image-generation — GPU 生图 (16 项 + MCP)

| # | 功能 | # | 功能 |
|---|------|---|------|
| 1 | 分镜预解析 | 9 | 像素级校验 |
| 2 | 角色形象锁定 | 10 | 局部重绘 |
| 3 | 画风模板 | 11 | 色调绑定 |
| 4 | 高清图像解析 | 12 | 批量绘图 |
| 5 | 三视图重建 | 13 | CLIP 语义校验 |
| 6 | PS 调度 (COM) | 14 | 素材归档 |
| 7 | SD 调度 (REST) | 15 | 高负载降级 |
| 8 | 引擎自动切换 | 16 | 联动接口 |

**MCP 桥接**：SD / Photoshop / SAI / Krita — 统一路由器自动检测与分发。

 ### 🟢 skill-blender-modeling — Blender 三维建模 (14 项 + MCP)
 
 | # | 功能 | # | 功能 |
 |---|------|---|------|
 | 1 | 项目初始化 | 8 | 粒子与物理 |
 | 2 | 基础建模(Polygon/SubD/NURBS) | 9 | 分镜联动 |
 | 3 | PBR 材质系统 | 10 | 参考图联动 |
 | 4 | 灯光系统(三点+HDRI) | 11 | 批量渲染 |
 | 5 | 摄像机与构图 | 12 | 资产库 |
 | 6 | 渲染引擎(Cycles+Eevee) | 13 | 高负载降级 |
 | 7 | 骨骼动画 | 14 | 联动接口 |
 
 **MCP 桥接**：bpy 调度核心 / 批量渲染队列 / 一键初始化。
 
 🖥️ 环境：Blender 5.1.2 (Steam) · RTX 4060 CUDA+OptiX · Cycles GPU 默认
 
 ### 🟢 skill-self-learning-expand — 自主学习 (8 项 + 扩容机制 + 视觉引擎)
 
 **常驻基础 5 Skill**：素材自动归集 / 合规检索 / 缺陷复盘 / 用户反馈 / 学习同步
 **资源兜底 3 Skill**：Token 阶梯限流 / 优先级调度 / 知识库隔离
 **自适应扩容**：新增拓展包自动生成专属学习子Skill + 扩充知识库类目
 
 **视觉分析引擎**：qwen-vl-plus (千问) + BLIP 本地备用，支持渲染图质量评估与建模反馈
 **RAG 向量库**：96 chunks, 4 分区 (kb_script/kb_image/kb_blender/kb_meta)
 
 ### 🟢 Qwen 生图管线 (外部依赖)
 
 | 模块 | 模型 | 功能 |
 |------|------|------|
 | 文本生图 | wan2.6-t2i | 参考图/三视图生成 |
 | 视觉分析 | qwen-vl-plus | 渲染图评估/建模反馈 |
 | API 底座 | DashScope | 自动 .env 加载 |
 
 > 已验证：狐狸四视图 1440x1440 · 渲染图比例/材质分析 · API 连通性 OK
 
 ### 🟢 skill-model-scoring — 模型评分 (5 项)

双层打分：裸模型基础分 (45%) + Agent 调度综合分 (55%)。低于 88 分自动触发补强兜底。

---

## 实测性能

| 引擎 | 模型 | 分辨率 | 耗时 |
|------|------|--------|------|
| GPU | SD 1.5 | 512×768 | 8.3s |
| GPU | Deliberate v2 | 512×768 | 11-15s |
| CPU | SD 1.5 | 512×512 | 135s |

> 硬件：NVIDIA RTX 4060 Laptop GPU, 4GB VRAM, fp16

---

## 快速开始

```bash
git clone https://github.com/CYFan8/OmniForge.git
```

详细文档见 [ARCHITECTURE.md](ARCHITECTURE.md) 和 [JOURNEY.md](JOURNEY.md)。

---



---

## 社区

<p align="center">
  <a href="https://github.com/CYFan8/OmniForge/discussions">
    <img src="https://img.shields.io/badge/Discussions-💬_加入讨论-blue" alt="Discussions">
  </a>
  <a href="https://github.com/CYFan8/OmniForge/issues">
    <img src="https://img.shields.io/badge/Issues-🐛_报告问题-red" alt="Issues">
  </a>
</p>

OmniForge 的灵魂不是代码，是**共建**。

每一个 Skill 都是一块积木——你写的剧本技巧、我调的生图参数、他踩的部署坑——拼在一起才叫「趋近全能」。

- **想贡献新 Skill？** Fork → 写一个 SKILL.md → PR。三步。
- **有问题或想法？** [Discussions](https://github.com/CYFan8/OmniForge/discussions) 里随便聊。
- **发现 Bug？** [Issues](https://github.com/CYFan8/OmniForge/issues) 提。
- **只是路过觉得有用？** 点个 Star ⭐ 就是最大的鼓励。

> 一个人能走得快，一群人能走得远。这个仓库不是我的，是每一个贡献者的。

---

## 文件目录


```
OmniForge/
├── README.md               ← 你在这里
├── ARCHITECTURE.md         ← 四层架构全景图
├── JOURNEY.md              ← 开发历程 + 23 个坑
├── CONTRIBUTING.md         ← 共建指南
├── CHANGELOG.md            ← 版本更新日志
 ├── VERSION                 ← v2.1
├── .gitignore
│
├── system-global-settings/ ← L1: 全局设置
│   ├── SKILL.md
│   └── system-config.yaml
│
├── skill-system-core/      ← L2: 17 项核心技能
│   └── SKILL.md
│
 ├── skill-script-creation/  ← L3: 剧本创作 (13项)
│   └── SKILL.md
│
 ├── skill-image-generation/ ← L3: GPU 生图 (16项 + MCP)
│   ├── SKILL.md
│   └── mcp/                ← MCP 桥接脚本
│       ├── router.py
│       ├── config.json
│       ├── sd_bridge.py
│       ├── photoshop_bridge.py
│       ├── sai_bridge.py
│       └── init.ps1
│
 ├── skill-blender-modeling/ ← L3: Blender建模 (14项 + MCP)
 │   ├── SKILL.md
 │   └── mcp/                ← bpy 调度 / 批量渲染
 │
 ├── skill-self-learning-expand/ ← L3: 自主学习 (8项 + 视觉引擎)
 │   ├── SKILL.md
 │   ├── references/          ← RAG知识库 4分区 (96 chunks)
 │   └── vision/              ← 千问视觉分析引擎
 │
 ├── skill-model-scoring/    ← L4: 模型评分 (5项)
│   └── SKILL.md
│
└── references/             ← 知识库
    ├── realism_kb/         ← RAG 写实知识库 (4KB)
    ├── sd_techniques.md
    ├── ai_image_techniques.md
    └── chinese_script_guide.md
```

---

## 共建

```bash
# 1. Fork → 2. 创建 skill-xxx/SKILL.md → 3. PR
```

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。每个 Skill 只需要一个 Markdown 文件。

---

## 踩坑实录

部署过程中遇到了 23 个实机问题——从 GitHub 被墙到 Python venv 丢失 ctypes 到破解版 PS COM 不可用。每条都有根因和解决方案，记录在：

- 各 SKILL.md 的「踩坑实录与解决方案」章节
- [JOURNEY.md](JOURNEY.md) — 完整开发历程

---

## 许可

MIT — 拿去用，改，分发。希望你觉得有用时也贡献回来。

---

 **CYFan8 · 2026 · OmniForge v2.1**
 
 ---
 
 ## 开发日志
 
 每日工作记录在 [`logs/`](logs/) 目录下。
 
 ### 2026-07-20 — v2.1 建模拓展包 + 自主学习 + Qwen管线
 
 **新增拓展包：**
 - `skill-blender-modeling` — Blender 3D 建模，14 项能力 + MCP bpy 桥接
 - `skill-self-learning-expand` — 自主学习，8 Skills + 扩容机制 + 视觉引擎
 
 **新增 Qwen 管线：**
 - 文本生图 (wan2.6-t2i) — 狐狸四视图参考图生成验证通过
 - 视觉分析 (qwen-vl-plus) — 渲染图比例/材质/建模反馈验证通过
 - 三视图生图管线：千问生成 → 混元3D → (待完善)
 
 **学习进度：**
 - kurtips Blender 建模课程 4 节字幕 (12 万+ 字符) 分析入库
 - 建模体块搭建核心流程 (Extrude/Inset/Loop Cut/Bevel) 掌握
 - RAG 知识库更新 96 chunks，4 分区
 
 **工程：**
 - 安装 Playwright chromium-1228 浏览器自动化
 - 混元3D 网页登录 + 图生3D 上传验证通过
 - 千问 API (DashScope) 连通，`qianwen-ai` 9 个技能包就绪
 
 **已知缺陷（v2.1）：**
 | 缺陷 | 严重度 | 说明 |
 |------|-------|------|
 | 系统 python 损坏 | P0 | PATH python exit code 1，需用 Codex runtime |
 | 混元3D 生成未完成 | P0 | 进度反复重置，需调试或换方案 |
 | 建模包 14 项脚本已实现 | P1 → ✅ | 12 个 Python 脚本 + bridge 调度器已提交 |
 | RAG 仅 96 chunks | P1 | 覆盖不够，需持续入库 |
 | 生图质量不稳定 | P2 | 无 seed，构图/内容随机 |
 | vision init 结构错误 | P2 | 类导入路径混乱 |
 | 无自动化测试 | P3 | 全部模块零测试覆盖 |
 
 完整日志：[logs/2026-07-20.md](logs/2026-07-20.md)
