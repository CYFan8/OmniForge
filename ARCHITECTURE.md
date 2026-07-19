# 四层架构全景图

> 生成时间: 2026-07-19
> 状态: 全部就绪，GPU Server 运行中

---

## 第一层：全局设置 (Global Agents)

| 组件 | 路径 | 条目 | 管控内容 |
|------|------|------|---------|
| **AGENTS.md** | `~\.codex\AGENTS.md` | 启动 6 步 | 角色定义、核心原则、记忆管理、Token 预算、调度逻辑、MCP 服务、双引擎工作流 |
| **system-global-settings** | `D:\ai_skill_lib\system-global-settings\` | 4 分区 | ①启动配置(开机扫描+舆情采集+缓存) ②模组隔离(数据隔离+联动断连+故障隔离) ③RAG配置(分区存储+文本压缩) ④评分阈值(合格线) |
| **system-config.yaml** | `D:\ai_skill_lib\system-global-settings\system-config.yaml` | 4 分区参数 | 可手动修改的运行时配置 |

**加载顺序**: L2画像 → 学习教训 → 改进假设 → 全局设置面板 → 核心技能包 → 注入 L4

---

## 第二层：底层核心技能包 (Core Skills)

| # | 技能 | 所属 Skill | 关键能力 | 依赖软件/库 |
|---|------|-----------|---------|------------|
| 1 | 开机自检 | skill-system-core | 并行扫描 PS/Krita/GIMP + 舆情采集 + 生成诊断报告 | pywin32 |
| 2 | 绘图软件分发 | skill-system-core | 推送合规下载渠道 → 无 PS 自动切 SD | — |
| 3 | 文档解析 | skill-system-core + skill-doc-parse | docx/xlsx/PDF → 自动分流至 RAG 分区 | python-docx, openpyxl, PyMuPDF |
| 4 | RAG 向量底座 | skill-system-core + skill-search-opt | 文本切片→Embedding→分区存储→检索 | chromadb, sentence-transformers |
| 5 | 双层记忆 | skill-system-core + skill-gcma-extend | 长期偏好(剧本风格/画面审美) + 短期任务缓存 | — |
| 6 | 工具更新 | skill-system-core | 后台静默检测 pixelmatch/CLIP/MCP 桥接版本 | — |
| 7 | Agent 调度 | skill-system-core | 统一调度图像识别/像素比对/绘图桥接 | — |
| 8 | 上下文压缩 | skill-system-core | 大型文档仅传 ID，原始数据不入上下文窗口 | — |
| 9 | 模组互联锁 | skill-system-core | 版本兼容校验 + 资源冲突检测 + 通道销毁 | — |
| 10 | 弹性 Token 管控 | skill-system-core | 分层配额 35000→+4000/拓展→封顶50000 | — |
| 11 | 低分兜底 | skill-system-core | 自动补强 → 重核算 → 轻量降级 / 智能模型推荐 | — |
| 12 | 日志系统 | skill-system-core | 全链路事件采集 + 24h 分档 + TXT 导出 | — |
| 13 | 素材导入导出 | skill-system-core | 批量图片/Excel/PDF/TXT + 完整性校验 + 自动分流 | — |
| 14 | 外网限流 | skill-system-core | 自适应请求间隔 + 失败重试 2 次 | requests, httpx |
| 15 | 模型切换 | skill-system-core | 留存全部配置 → 重算评分 → 自适应调度参数 | — |
| 16 | GitHub 仓库检索 | skill-system-core | 跳转技能仓库 + 屏蔽恶意捆绑 | — |
| 17 | 技能归属判定 | skill-system-core | 四维判定(耦合度/算力/依赖/业务域)→自动归类 | — |

### 引用知识库

| 编号 | 文件 | 标签 | 用途 |
|------|------|------|------|
| KB001 | `references/realism_kb/kb001_human_anatomy.md` | #anatomy #human | 人体比例/肌肉/面部 |
| KB002 | `references/realism_kb/kb002_lighting_materials.md` | #lighting #materials | 三点布光/金属/布料 |
| KB003 | `references/realism_kb/kb003_composition_camera.md` | #composition #camera | 三分法/焦段/色彩 |
| KB004 | `references/realism_kb/kb004_animal_anatomy.md` | #animal #canine | 犬科/猫科/鸟类 |
| — | `references/sd_techniques.md` | #sd #prompt | SD 1.5 提示词技巧 |
| — | `references/ai_image_techniques.md` | #anime #realistic | AI 生图完整技巧 |
| — | `references/chinese_script_guide.md` | #script #chinese | 中文剧本规范 |
| — | `JOURNEY.md` | #journal | 完整开发历程 + 23 个坑 |

---

## 第三层：业务拓展模组 (Extension Skills)

### 剧本创作拓展包 — `skill-script-creation`

| # | 功能 | 说明 | 依赖 |
|---|------|------|------|
| 1 | 世界观归档 | 全文语义扫描 → 持久存储人物/场景/时间线 | — |
| 2 | 冲突校验 | 识别人设矛盾/场景逻辑冲突/时间线错位/道具不统一 | — |
| 3 | RAG 剧情检索 | 同题材/同风格参考文本检索 | skill-search-opt |
| 4 | 台词校准 | 按年龄/身份/性格匹配对话语气和句式 | — |
| 5 | 多分支推演 | 主线 → 多条平行故事分支 | — |
| 6 | 节奏分析 | 量化冲突密度 → 标注平淡/过密段落 | — |
| 7 | 伏笔梳理 | 汇总隐藏伏笔 + 对应回收节点 | — |
| 8 | 剧本格式化 | 院线电影 + 短视频短剧双格式 | — |
| 9 | 批量导出 | TXT/PDF 双格式，自动区分场景/台词/动作 | python-docx, reportlab, fpdf2 |
| 10 | 分镜生成 | 拆分场景/人物/镜头 → 标准化分镜文本 | — |
| 11 | 跨包推送 | 临时开启接口 → 向生图模组单向推送数据 | — |
| 12 | 时间线纠错 | 检测并修正时序错乱 | — |
| 13 | 道具统一 | 持久存储道具清单 + 全文一致性校验 | — |

### 生图联动拓展包 — `skill-image-generation`

| # | 功能 | 说明 | 绑定引擎 |
|---|------|------|---------|
| 1 | 分镜预解析 | 剧本文本 → 分层精细化绘图提示词 | SD / PS |
| 2 | 角色锁定 | RAG 人物向量 → 锁定五官/体型/服饰 | SD / PS |
| 3 | 画风模板 | 写实/电影质感/二次元/国风 四套模板 | SD |
| 4 | 图像解析 | 局部裁切放大 → 提取配色/尺寸参数 | SD |
| 5 | 三视图重建 | 道具/建筑三视图 → 彩色概念效果图 | SD |
| 6 | PS 调度 | MCP 桥接 Photoshop → Firefly AI 绘图 | PS (正版) |
| 7 | SD 调度 | MCP 桥接 SD WebUI → txt2img/img2img | SD |
| 8 | 引擎切换 | 自动检测可用工具 → 按优先级路由 | Router |
| 9 | 像素校验 | pixelmatch 量化比对 → 自定义差异阈值 | pixelmatch |
| 10 | 局部重绘 | 缺陷区域定位 → 自动优化提示词重绘 | SD |
| 11 | 色调绑定 | 参考图配色提取 → 统一全部生成画面 | SD |
| 12 | 批量绘图 | 整本剧本统一光影/色调/透视出图 | SD |
| 13 | CLIP 校验 | 画面内容 vs 文本提示词匹配度检测 | CLIP |
| 14 | 素材归档 | 按剧本/人物/场景分类存储 | — |
| 15 | 高负载降级 | 算力不足 → 关闭像素校验 → 文字语义匹配 | — |
| 16 | 联动接口 | 接收剧本模组推送的人设/分镜数据 | — |

### MCP 桥接

| Bridge | 目标 | 方式 | 状态 |
|--------|------|------|------|
| sd_bridge | Stable Diffusion / Deliberate v2 | GPU REST API (:7861) | ✅ 运行中 |
| photoshop_bridge | Adobe Photoshop | COM Automation | ❌ 破解版不可用 |
| sai_bridge | PaintTool SAI/SAI2 | Filesystem | ✅ 就绪 |
| router | 统一路由 | 检测→分发→回退 | ✅ 就绪 |

---

## 第四层：通用模型评分机制 (Model Scoring)

| # | 功能 | 说明 | 关键指标 |
|---|------|------|---------|
| 1 | 裸模型评测 | 独立评测大模型原生能力(不加载任何插件) | 5 维度 × 45% 权重: 长文本理解/逻辑推理/文本创作/提示词生成/文档解析 |
| 2 | 综合打分 | 大模型 + Agent 调度 + 全套插件协同得分 | 6 维度 × 55% 权重: RAG调度/工具校验/MCP桥接/像素比对/批量处理/软件分发 |
| 3 | 分层补强 | 按得分区间差异化补齐工具 | <78 全量安装 / 78-88 精简核心 / 88-95 轻量校准 |
| 4 | 低分兜底 | 补强后仍未达标 → 两套方案 | 方案A: 轻量化降级 / 方案B: 智能适配模型推荐 |
| 5 | 配套资源联动约束 | 评分记录写日志 + 外网限流复用 + 调分约束清洗 | 单日±5 分浮动 / 7 日滚动均值平滑 |

### 评分流程

```
裸模型评测(45%) + 综合打分(55%)
        ↓
  低于合格阈值(默认88)?
    YES → 分层补强 → 重算
        ↓
    仍未达标?
      YES → 诊断报告 → 方案A/B
```

---

## 当前运行状态

| 组件 | 状态 | 详情 |
|------|------|------|
| GPU Server | 🟢 运行中 | :7861, Deliberate v2 |
| SD 1.5 模型 | 🟢 已部署 | 4GB, 写实向 |
| Deliberate v2 模型 | 🟢 已部署 | 2GB, 写实+二次元 |
| MCP Router | 🟢 就绪 | 自动检测+路由 |
| SAI Bridge | 🟢 就绪 | 文件系统桥接 |
| PS Bridge | 🔴 不可用 | 破解版 COM 缺失 |
| 4 知识库 | 🟢 就绪 | RAG 可检索 |
| 23 个坑 | 📝 已归档 | JOURNEY.md + 2 Skill 踩坑实录 |
