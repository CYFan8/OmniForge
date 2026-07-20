# OmniForge 全套模块化 Skill 总文档 v2.0

> 生成时间: 2026-07-20
> 状态: 全模块就绪 — 4 组拓展包 + 自主学习核心 + GPU Server 运行中

---

## 整体架构规则

1. **分层结构**: 全局设置模块（固定底层）→ 底层基础技能包（必备核心）→ 多组可插拔业务拓展包（相对隔离，按需联动）
2. **联动约束**: 无用户指定联动指令时各模块独立运行，互不干扰；主动下发联动指令后通过MCP协议互通数据
3. **拓展兼容**: 新增任意业务拓展包时，自主学习拓展包自动生成配套学习子技能、扩充对应知识库类目
4. **统一管控**: 全模块共用全局Token弹性配额、裸模型动态评分机制、RAG切片向量化底层内置逻辑

---

## 一、全局设置模块（固定内置，不可卸载）

| # | Skill | 路径/所属 | 功能说明 |
|---|-------|---------|---------|
| 1 | 开机自检Skill | skill-system-core | 自动扫描本地安装的大模型、SD WebUI、PS/SAI、Blender；爬取全网大模型、Agent用户风评，动态更新40~100分段裸模型基础评分 |
| 2 | Context路由切换Skill | skill-system-core | 全局开关一键屏蔽原生OpenAI图像鉴权绑定，强制生图、3D渲染请求走本地MCP对接绘图/建模软件，无需OpenAI Key |
| 3 | 跨大模型兼容Skill | skill-system-core | 解除单一模型绑定限制，Codex Agent可自由调度任意国产/开源大模型，统一适配全技能包调用逻辑 |
| 4 | 全局弹性Token管控Skill | skill-system-core | 单独限制检索类Token消耗，阶梯式扩容；新增拓展包自动上调模块总Token上限，防止过量检索造成模型幻觉 |
| 5 | 软件安全下载引导Skill | skill-system-core | 检测缺失PS、SAI、Blender等工具时弹窗询问用户，提供国内安全镜像渠道；用户拒绝下载则直接屏蔽对应绘图/建模链路 |

**运行时配置**: system-config.yaml（启动扫描/模组隔离/RAG分区/评分阈值）

---

## 二、底层基础技能包（核心必备，可临时禁用）

| # | Skill | 所属/关联 | 功能说明 |
|---|-------|---------|---------|
| 1 | RAG知识库底层处理Skill | skill-system-core + skill-search-opt | 内置文本切片、向量化存储逻辑，无独立技能标识，全模块通用，统一存储剧本、人体解剖、三渲二工艺、建模教程等素材 |
| 2 | 自定义Skill分类判定Skill | skill-system-core | 识别GitHub下载、AI自研的第三方技能模组，自动划分归属：基础包/独立拓展包/全新拓展包 |
| 3 | 任务熔断防护Skill | skill-system-core | 拦截超长推理、循环请求，防止无限制消耗Token，任务超时自动降级兜底 |
| 4 | 统一文件读写导出Skill | skill-system-core + skill-doc-parse | 标准化读取、输出剧本、三视图、建模参考图、Blender配置、渲染底图、学习日志文件 |
| 5 | 双层综合评分计算Skill | skill-model-scoring | 权重分配：裸模型45% + Agent+技能附加分55%；总分低于88分时自动启动多阶补强流程 |
| 6 | GitHub开源技能检索Skill | skill-system-core | 内置ghproxy镜像解决终端访问限制，跳转官方技能资源页，安全下载开源拓展模组 |

---

## 三、可插拔业务拓展包（相互隔离，支持联动）

### 拓展包 1: 剧本创作 — skill-script-creation

| # | Skill | 功能 |
|---|-------|------|
| 1 | 剧本知识库构建Skill | 自动生成人物设定、世界观、时间线、短剧分镜文本，自动校验剧情、人设逻辑冲突 |
| 2 | 跨模块数据推送Skill | 导出人设、场景、道具文字数据，同步推送至生图拓展、Blender建模拓展包生成配套资产 |

**完整能力**: 世界观归档/冲突校验/RAG剧情检索/台词校核/多分支推演/节拍分析/伏笔梳理/格式化导出/分镜生成/跨包推送/时间线纠错/道具统一（13项）

---

### 拓展包 2: AI生图 — skill-image-generation

| # | Skill | 功能 |
|---|-------|------|
| 1 | 快速直绘Skill | 输入提示词直接生成写实图像，适用于简易概念草图 |
| 2 | Reference-to-3D参考图转三视图Skill | 上传单张参考图，AI解析物体结构，生成正面/侧面/背面三视图，附带尺寸标注文件，直接供给Blender建模 |
| 3 | Model-to-Image建模前置生图Skill | 读取Blender基础模型渲染线稿、灰度底图，仅优化材质、光影、写实质感，锁死3D原有结构，杜绝肢体、透视崩坏（效果差自动切换兜底链路） |
| 4 | 专业绘图软件联动Skill | 生成图像自动分层推送PS、SAI完成精细化后期调整 |

**完整能力**: 分镜预解析/角色锁定/画风模板/图像解析/三视图重建/PS调度(MCP)/SD调度(MCP)/引擎切换/像素校验/局部重绘/色调绑定/批量绘图/CLIP校验/素材归档/高负载降级/联动接口（16项 + MCP桥接）

**MCP 桥接状态**:

| Bridge | 目标 | 方式 | 状态 |
|--------|------|------|------|
| sd_bridge | Stable Diffusion / Deliberate v2 | GPU REST API (:7861) | 运行中 |
| photoshop_bridge | Adobe Photoshop | COM Automation | 不可用（破解版） |
| sai_bridge | PaintTool SAI/SAI2 | Filesystem | 就绪 |
| router | 统一路由 | 检测→分发→回退 | 就绪 |

---

### 拓展包 3: Blender三维建模 — skill-blender-modeling

| # | Skill | 功能 |
|---|-------|------|
| 1 | Blender本地环境自检适配Skill | 自动检测CUDA加速、必备插件，缺失资源自动跳转安全渠道下载 |
| 2 | 三视图导入建模Skill | 读取生图包输出的三视图，自动生成基础体块模型，锁定人物、场景、道具尺寸比例 |
| 3 | 三渲二NPR渲染工艺Skill | 输出分层明暗线稿、二分色底图，输送至生图拓展包叠加写实细节 |
| 4 | 3D资产标准化导出Skill | 导出建模参数、镜头配置、渲染参考图，可回传生图模块复用资产风格 |

**完整能力**: 项目初始化/基础建模(Polygon+SubD+NURBS)/PBR材质系统/灯光系统(三点布光+HDRI)/摄像机与构图/渲染引擎(Cycles GPU+Eevee)/骨骼动画/粒子与物理/分镜联动/参考图联动/批量渲染/资产库/高负载降级/联动接口（14项 + MCP桥接）

**MCP 桥接状态**:

| Bridge | 目标 | 方式 | 状态 |
|--------|------|------|------|
| blender_bridge | Blender 5.1.2 (Steam) | bpy subprocess | 运行中 |
| render_queue | 批量渲染 | 并行分片+断点续渲 | 就绪 |

**环境信息**:

| 项目 | 值 |
|------|-----|
| Blender 版本 | 5.1.2 (Steam, F:\steam\steamapps\common\Blender\) |
| GPU | NVIDIA GeForce RTX 4060 Laptop (CUDA + OptiX) |
| 渲染引擎 | Cycles GPU（默认）/ Eevee（降级） |

---

### 拓展包 4: 自主学习 — skill-self-learning-expand

#### 4.1 常驻基础Skill（永久内置，不随拓展增减变化）

| # | Skill | 功能 |
|---|-------|------|
| 1 | 全模块素材自动归集Skill | 扫描本地所有模块产出文件：剧本文档、生图图集、Blender工程、渲染素材、配置参数，自动分类切片、向量化入库 |
| 2 | 合规公开素材检索Skill | 仅爬取免费行业教程、开源案例，设置单轮检索Token上限；新增拓展包自动匹配对应领域检索关键词 |
| 3 | 全链路缺陷复盘记录Skill | 捕捉生图崩坏、建模透视错误、剧本逻辑漏洞、三渲二光影失真，生成标准化缺陷样本库作为学习素材 |
| 4 | 用户反馈采集迭代Skill | 开机同步爬取GitHub、技术论坛用户评价，动态调整裸模型评分、各技能权重；新增拓展包自动新增对应反馈分类 |
| 5 | 学习成果全局同步Skill | 完成专项学习后，自动更新对应拓展包的提示词模板、参数阈值、知识库素材，全链路同步优化输出效果 |

#### 4.2 自适应动态扩容机制（核心特性）

系统实时检测已安装业务拓展包列表，每新增一款拓展包，自动追加专属学习子Skill、扩充独立知识库类目，无需手动修改配置。

**当前已匹配 4 组拓展包专属学习子Skill:**

| 匹配拓展包 | 专属学习子Skill |
|-----------|---------------|
| 剧本 (Pack 1) | 剧本叙事逻辑 / 人物塑造 / 短剧分镜文案 / 世界观搭建 |
| 生图 (Pack 2) | 人体动物写实解剖 / 光影材质 / 三视图结构还原 / 建模前置生图逻辑 |
| Blender建模 (Pack 3) | 硬表面建模 / 体块搭建 / 三渲二分层渲染 / 镜头透视控制 |
| 自身 (Pack 4) | 素材分类算法 / Token限流策略 / 跨模块数据互通规则 / 学习效率自评 |

**扩容规则（后续新增拓展包自动生效）**:

若新增音频配音、动画分镜等拓展包：
1. 自主学习包自动生成该模块专属学习子Skill
2. 新增对应行业素材检索标签、知识库分类
3. 新增专项缺陷捕捉、复盘逻辑
4. 学习完成后自动向新拓展包下发优化参数、模板

#### 4.3 资源兜底管控Skill

| # | Skill | 功能 |
|---|-------|------|
| 1 | 学习任务Token阶梯限流Skill | 新增大量学习类目时，平缓上调本模块总Token配额，隔离检索消耗，不挤占创作类拓展包资源 |
| 2 | 学习任务优先级调度Skill | 用户当前正在使用的拓展包，对应学习任务优先占用算力；闲置拓展包学习任务降低资源分配 |
| 3 | 学习知识库隔离Skill | 不同拓展包对应的学习素材、训练参数分库独立存储，避免跨领域知识混淆引发输出错误 |

---

## 四、全局通用联动规则

| # | Skill | 功能 |
|---|-------|------|
| 1 | 模块隔离防护Skill | 无用户联动指令时，所有业务拓展包独立运行，数据互不互通，规避跨模块逻辑报错 |
| 2 | 手动联动触发Skill | 用户下发联动指令后，通过MCP协议打通模块数据流，支持完整流水线：剧本→生图三视图→Blender建模→三渲二渲染→建模驱动风格化生图 |
| 3 | 模块故障自动降级Skill | 单一拓展包功能失效时，自动切换备用链路；如生图拓展效果不佳，自动启用Blender建模前置再生图模式 |

**联动管线示意**:

`
skill-script-creation (剧本)
  ├──→ 分镜+人设数据 ──→ skill-image-generation (生图)
  │                          ├──→ 参考图/三视图 ──→ skill-blender-modeling (3D建模)
  │                          │                         └──→ 线稿/灰度底图 ──→ skill-image-generation (再生图)
  │                          └──→ 分层图 ──→ PS/SAI (后期)
  │
  └──→ 剧本参数 ──→ skill-self-learning-expand (自主学习)
                       └──→ 优化参数 ──→ 回写各拓展包 SKILL.md / references/

skill-model-scoring (评分)
  └──→ 全模块质量评估 → 低于88分触发补强 → 联动自主学习包迭代
`

---

## 当前运行状态

| 组件 | 状态 | 详情 |
|------|------|------|
| GPU Server | 运行中 | :7861, Deliberate v2 |
| SD 1.5 模型 | 已部署 | 4GB, 写实向 |
| Deliberate v2 模型 | 已部署 | 2GB, 写实+二次元 |
| Blender 5.1.2 | 运行中 | Steam, RTX 4060 CUDA+OptiX |
| MCP Router (生图) | 就绪 | 自动检测/路由 |
| MCP Bridge (Blender) | 运行中 | bpy 调度核心，测试通过 |
| SAI Bridge | 就绪 | 文件系统中转 |
| PS Bridge | 不可用 | 破解版 COM 缺失 |
| 4 组拓展包 | 全部就绪 | 剧本/生图/建模/自主学习 |
| 知识库 | 就绪 | 4 库 RAG 可检索 |

---

## 技能目录总览

`
OmniForge/
├── AGENTS.md                          → L0: 核心调度
├── ARCHITECTURE.md                    → 本文档
├── README.md
├── CHANGELOG.md
├── JOURNEY.md
├── VERSION                            → v2.0
│
├── system-global-settings/            → L1: 全局设置（5 Skills）
│   ├── SKILL.md
│   └── system-config.yaml
│
├── skill-system-core/                 → L2: 底层核心（17项调度能力）
│   └── SKILL.md
│
├── skill-script-creation/             → L3: 剧本创作（13项）
│   └── SKILL.md
│
├── skill-image-generation/            → L3: AI生图（16项 + MCP）
│   ├── SKILL.md
│   └── mcp/                           → SD/PS/SAI/Router 桥接
│
├── skill-blender-modeling/            → L3: Blender建模（14项 + MCP）
│   ├── SKILL.md
│   └── mcp/                           → bpy调度/批量渲染/初始化
│
├── skill-self-learning-expand/        → L3: 自主学习（8 Skills + 扩容）
│   ├── SKILL.md
│   └── references/
│
├── skill-model-scoring/               → L4: 模型评分（5项）
│   └── SKILL.md
│
├── skill-search-opt/                  → 检索增强（三级检索）
├── skill-doc-parse/                   → 文档解析
├── skill-gcma-extend/                 → 记忆系统
├── skill-code-review/                 → 代码审查
├── skill-self-optimize/               → 自我优化
├── skill-ui-writing/                  → UI文案
├── skill-math-model/                  → 数学建模
├── skill-finder/                      → 技能发现
│
└── references/                        → 共享知识库
    ├── realism_kb/                    → 写实知识库(4 KB)
    ├── sd_techniques.md
    ├── ai_image_techniques.md
    └── chinese_script_guide.md
`

---

## 版本变更

### v2.0 (2026-07-20)
- 新增: 拓展包 3 — Blender三维建模（14 Skills + MCP bpy桥接）
- 新增: 拓展包 4 — 自主学习拓展包（8 Skills + 自适应扩容机制）
- 更新: 全局设置模块 → 新增Context路由切换、跨大模型兼容、软件安全下载引导
- 更新: 系统配置纳入建模拓展模组隔离规则
- Blender 5.1.2 桥接烟雾测试通过（RTX 4060 CUDA + OptiX）

### v1.0 (2026-07-19)
- 初始发布: 全局设置 + 核心技能包 + 剧本/生图双拓展 + 模型评分
- GPU Server 部署完成（SD 1.5 + Deliberate v2）
