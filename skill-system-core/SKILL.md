---
name: skill-system-core
description: >-
  系统底层基础核心技能包，承载全系统通用底层调度、网络管控、故障运维、
  资源适配、技能归属判别、第三方拓展兼容能力。后台静默运行，全部逻辑受
  全局设置参数约束。当需要执行系统自检、工具调度、Token管控、日志记录、
  素材导入导出、模型切换等底层操作时激活。每次启动自动加载。
---

# 底层基础核心技能包（17项）

## 1. 开机自检

校验软件环境并生成完整诊断报告。完全依从全局设置启动开关运行，并行执行本地绘图软件扫描（Photoshop/Krita/GIMP三类安装目录检索）、全网舆情采集（技术社区、创作类论坛）两大子流程，配套本地持久化缓存机制，严格遵循全局配置的缓存生命周期复用存量数据。自检结束后自动生成结构化诊断报告，完整输出：绘图软件安装状态（已安装/未安装/版本号）、舆情数据更新记录（采集时间/来源/有效评价数）、当前大模型与Agent全维度评分明细。

## 2. 绘图软件分发

合规推送绘图工具，自动切换开源链路。系统自检识别本地无合规绘图软件时弹出交互确认窗口，仅推送软件官方站点（Adobe Photoshop官网、Krita官网、GIMP官网）、开源合规GitHub仓库两类下载渠道，附带标准化安全安装指引。屏蔽破解版、捆绑第三方插件的非正规资源。用户选择放弃下载时，永久断开Photoshop Firefly桥接链路，自动切换本地Stable Diffusion开源绘图链路，完整保留生图模组全部基础图像生成能力。

## 3. 文档解析

读取多格式文件并分类存入向量库。弥补大模型原生文件解析缺陷，支持docx、xlsx、PDF标准化解析，精准提取剧本文本、人设表格、三视图配套描述文本。解析完成后自动识别素材业务属性，自动分流至RAG向量库对应剧本/图像独立分区存储。

## 4. RAG向量底座

文本切片编码，缓存高频素材。严格遵循全局素材分区隔离配置执行存储策略，内置标准化闭环RAG处理链路：素材文件导入→文档解析→语义文本分块切片→Embedding向量编码→分区持久化存储。对高频复用人设、标准绘图提示词、经典剧本段落设置永久缓存，规避重复切片、向量化计算损耗算力。内置检索链路独立Token限额管控，协同全局文本摘要压缩机制双重控制资源消耗，降低语义幻觉概率。

## 5. 双层记忆

区分长期偏好与单次临时任务数据。划分为长时记忆、短时记忆两套独立存储单元。长时记忆分域持久存储用户长期使用偏好，区分剧本行文风格（文风偏好、叙事节奏、对白密度）与画面光影审美（色调倾向、构图偏好、光影强度）两类数据。短时记忆仅缓存单次任务交互问答、临时素材参数，任务执行完毕自动清空，持续上下文堆积造成的算力与Token冗余。

## 6. 工具更新

静默检测组件版本，自动兼容升级。后台定时静默执行版本校验，自动检测以下组件的官方更新包：像素比对工具（pixelmatch）、图像识别组件（CLIP/ResNet等）、MCP软件桥接服务（Photoshop MCP桥接、Stable Diffusion桥接）。检测到新版本后自动完成下载、兼容适配、覆盖更新。更新失败将异常信息写入运行日志，不中断前台正在执行的业务任务。

## 7. Agent调度

统一管控图像、绘图各类外部工具。作为全系统工具调度核心，统筹图像识别、像素比对、绘图软件桥接全部外部工具。无强制推理时长截断机制，适配不同复杂度、篇幅的差异化任务，不会强制终止未完成任务。内置自适应循环约束阈值：单张图像迭代重绘上限3轮，单次任务Agent总执行步数上限20步，可依据任务规模动态自适应调整，平衡运行效果与资源开销。

## 8. 上下文压缩

仅传素材ID，减少token占用。系统对大型文档、高清参考图执行轻量化预处理，仅向大模型传输素材本地唯一标识ID，完整原始文本、图像二进制编码不注入模型上下文窗口，从底层削减算力负载与Token消耗。永久默认启用，无手动开关。

## 9. 模组互联锁

检测拓展包冲突，管控跨包通道。后台自动完成拓展包版本兼容性校验、同类模组资源互斥冲突检测。识别版本不匹配、端口/算力抢占冲突时弹窗告警。剧本、生图模组的数据互通、通道销毁逻辑完全跟随全局隔离配置执行，无需人工干预底层数据传输调度。

## 10. 弹性Token管控

动态分配额度，超限自动精简文本。内置分层单次任务Token配额规则：仅启用剧本、生图两套基础拓展时单次任务Token上限35000；每新增一套第三方拓展模组配额上浮4000；设置全系统永久Token封顶值50000，杜绝资源无限占用。配套分级降级策略：Token消耗达到总配额80%时自动精简内外检索文本；触及全局封顶阈值时直接关闭全部外网检索链路，优先保障核心业务任务持续运行。

## 11. 低分兜底

自动补全工具，提供降级运行方案。后台自动完成全套配套插件、绘图工具的自动下载与环境补强。补强完成后重新核算模型综合评分；若得分仍低于全局设置合格阈值，自动弹出结构化诊断报告，完整标注未达标刚需维度、系统全部补强操作记录。提供两套可选处置方案：方案一轻量化降级运行，关闭高精度像素校验、批量图像生成等高消耗功能，仅保留剧本撰写、单图简易生成基础能力；方案二智能适配模型推荐，筛选裸模型基础分≥82分的适配模型，支持一键切换，原有RAG向量库全部素材、用户全局配置完整复用，无需重复导入素材。

## 12. 日志系统

全流程记录事件，支持日志导出排查。全程静默采集全链路运行事件，包含：舆情爬取记录（时间/来源/采集量）、RAG检索资源消耗（Token消耗/检索次数/命中率）、Agent执行报错（错误类型/堆栈/上下文快照）、跨模组通道中断（中断时间/涉及模组/恢复状态）、绘图桥接崩溃（桥接类型/错误码/重试次数）、Token超限预警（当前消耗/配额上限/触发降级时间）。日志按24小时分档持久化存储，支持一键导出TXT日志文件，用于故障溯源排查。

## 13. 素材导入导出

批量读写文件，校验文件完整性。统一承载全系统文件读写底层能力，支持批量导入图片（PNG/JPG/PSD/TIFF）、Excel（xlsx/csv）、PDF、TXT文件。支持批量导出完整剧本（TXT/PDF双格式）、生成原画（PNG/PSD）、向量知识库全量备份文件。内置文件完整性校验机制，素材损坏、格式不兼容时弹窗提示，不直接中断任务。导入成功素材自动识别业务属性，分流至RAG对应存储分区。

## 14. 外网限流

控制网络请求频率，失败自动重试。统一管控系统全部外网访问行为，包含舆情采集、GitHub仓库访问、工具下载、模型接口调用。内置自适应请求间隔，多线程并行外网任务自动错开访问时序，规避高频请求触发平台风控限制。单次外网请求失败自动重试2次，重试失败终止流程并写入日志。该机制仅约束线上外网请求，本地离线文件处理、本地知识库检索不受限制。

## 15. 模型切换

适配不同大模型，复用全部用户配置。用户切换目标大模型时系统完整留存本地全部素材缓存、全局设置面板所有配置。自动重新计算新模型裸分、综合评分。自适应调整Agent调度中枢运行参数，适配新模型上下文窗口、推理特性，规避切换模型后模组功能失效、素材读取异常问题。

## 16. GitHub仓库跳转

检索下载第三方自定义技能。用户发起第三方技能检索、下载需求时，系统自动跳转专属开源GitHub技能仓库页面，支持在线浏览、下载剧本辅助插件、图像美化模组、通用功能拓展。复用外网限流容错机制，限制高频重复刷新仓库页面。屏蔽非开源、携带恶意捆绑程序的不合规资源，仅允许开源合规GitHub仓库来源。用户仓库访问、拓展下载操作自动写入系统运行日志持久留存。

## 17. 技能归属判定

自动划分技能归入基础/拓展包。两类场景自动启动全维度自动化判别：用户通过GitHub仓库下载外部第三方Skill脚本；用户调用AI自主生成全新自定义Skill程序。系统自动解析脚本全部代码逻辑、依赖环境、业务覆盖域、算力开销、底层耦合关系。基于四层标准化判定维度（底层耦合度、算力与资源开销、外部依赖、业务覆盖域）无人工介入自动完成归类判定。判定完成后自动完成文件目录迁移、依赖环境预安装、模组注册录入；若判定为全新独立拓展包，自动生成独立配置文件、独立日志分区、独立RAG素材存储目录，实现完全物理隔离。

---

## 依赖清单

### 绘图软件（模块2、7使用）
| 软件 | 用途 | 获取方式 |
|------|------|---------|
| Photoshop CC 2021+ | 专业分层绘图 + Firefly AI | Adobe官网订阅 / 合规授权 |
| Krita 5.0+ | 开源数字绘画 | krita.org 免费下载 |
| GIMP 2.10+ | 开源图像处理 | gimp.org 免费下载 |
| Stable Diffusion WebUI / ComfyUI | 开源AI绘图引擎 | GitHub开源仓库，自动脚本安装 |

### 文档解析库（模块3使用）
| 库 | 用途 | 安装命令 |
|----|------|---------|
| python-docx | DOCX解析 | `pip install python-docx` |
| openpyxl | XLSX解析 | `pip install openpyxl` |
| PyMuPDF (fitz) | PDF高速解析 | `pip install PyMuPDF` |
| pypdf | PDF提取 | `pip install pypdf` |

### 工具链（模块6使用）
| 组件 | 用途 | 安装命令 |
|------|------|---------|
| pixelmatch | 像素级图像比对 | `npm install pixelmatch` |
| opencv-python | 图像识别预处理 | `pip install opencv-python` |
| torch + torchvision | CLIP图像语义理解 | `pip install torch torchvision` |
| MCP Photoshop Bridge | PS MCP桥接服务 | GitHub自动拉取最新Release |

### 网络与存储（模块4、14使用）
| 组件 | 用途 | 安装命令 |
|------|------|---------|
| chromadb | 向量数据库存储 | `pip install chromadb` |
| sentence-transformers | Embedding向量编码 | `pip install sentence-transformers` |
| requests / httpx | 外网请求管控 | `pip install requests httpx` |

### 初始化脚本
首次部署时执行以下脚本自动安装全部Python依赖：
```
pip install python-docx openpyxl PyMuPDF pypdf opencv-python torch torchvision chromadb sentence-transformers requests httpx
npm install pixelmatch
```
绘图软件需用户手动下载安装，脚本仅检测安装状态并提示。

---

## 规则联动

- 全部逻辑 -> 受 system-global-settings 全局设置参数约束
- 文档解析(3) -> 调用 skill-doc-parse 全格式解析能力
- RAG检索(4) -> 联动 skill-search-opt 三级检索体系
- 双层记忆(5) -> 联动 skill-gcma-extend 双时态与账本
- 低分兜底(11) -> 触发 skill-model-scoring 评分重核算
- 模型切换(15) -> 联动 skill-model-scoring 重新评分
- 上下文压缩(8) -> 协同 Token管控防幻觉
- 开机自检(1) -> 为 skill-model-scoring 提供舆情数据源
- **Prompt 工程 -> 参考 references/sd_techniques.md 技巧库**

---

## RAG 写实知识库

> 路径: D:\ai_skill_lib\references\realism_kb\
> 用途: 生图时检索对应领域的解剖/光影/构图知识，注入 Prompt

| 编号 | 文件 | 标签 | 用途 |
|------|------|------|------|
| KB001 | kb001_human_anatomy.md | #anatomy #human #face #pose | 人物生图 |
| KB002 | kb002_lighting_materials.md | #lighting #materials #shadows | 光影材质 |
| KB003 | kb003_composition_camera.md | #composition #camera #lens #DOF | 构图镜头 |
| KB004 | kb004_animal_anatomy.md | #animal #canine #feline #bird | 动物生图 |
| - | index.md | RAG 检索入口 | 按标签匹配 KB |


---

## 踩坑实录与解决方案

> 以下问题均在 2026-07-19 实机部署中遇到并解决。

### Python 环境

| 问题 | 现象 | 根因 | 解决 |
|------|------|------|------|
| venv 隔离导致 ctypes 丢失 | `ModuleNotFoundError: No module named ctypes` | venv Python 继承了 runtime 全局 site-packages 但又隔离了 DLLs | **不要创建 venv**。直接用 runtime Python (`C:\Users\{user}\.cache\codex-runtimes\...\python.exe`)，内置 CUDA torch 2.6.0+cu124 |
| torch 是 CPU 版 | `CUDA available: False` | 清华镜像 pip install 的 torch 标注 `+cpu` | 检查 runtime Python 自带的 torch；或用户手动下载 CUDA wheel，用 `pip install xxx.whl` 安装 |
| PATH 缺少 DLLs | `import torch` 失败 | Codex runtime Python 的 DLLs 目录不在 PATH | 启动前 `set PATH={runtime}\DLLs;{runtime};%PATH%` |
| PYTHONHOME 设错 | `ModuleNotFoundError: No module named encodings` | PYTHONHOME 指向 venv 导致 stdlib 丢失 | 不设 PYTHONHOME，用 sys.path.insert 代替 |

### Shell 问题

| 问题 | 现象 | 根因 | 解决 |
|------|------|------|------|
| PowerShell 写文件编码错误 | Python 报 `SyntaxError: invalid character` | GBK 编码破坏 UTF-8 中文字符 | 用 Node REPL 的 `fs.writeFileSync` 写入；或全部改用英文注释 |
| cmd /c 引号冲突 | 复杂 Python 命令被截断 | PowerShell 和 cmd 的引号解析规则不同 | 把命令写入 .bat 文件，然后 `cmd /c file.bat` |
| Start-Process 不传环境变量 | 后台进程找不到 DLLs | Codex shell 的进程隔离策略 | .bat 文件开头显式 `set PATH=...` |

### 网络问题

| 问题 | 现象 | 根因 | 解决 |
|------|------|------|------|
| GitHub clone 全部超时 | `Connection reset / timeout` | GFW 阻断 | 放弃 git clone；改用 pip install + 用户手动下载模型 |
| HuggingFace 模型下载超时 | `ConnectTimeout` | huggingface.co 被墙 | 设 `HF_ENDPOINT=https://hf-mirror.com` |
| PyTorch CDN 下载超时 | `download.pytorch.org ReadTimeout` | CDN 也被墙 | 用户通过 PCL 百宝箱 → 自定义下载功能下载 wheel 文件 |
| 镜像文件不全 | `404 / 403` | hf-mirror 缓存不完整 | 换模型 repo 或让用户直接从镜像站下 |

### 模型部署

| 问题 | 现象 | 根因 | 解决 |
|------|------|------|------|
| `from_single_file` 仍需联网 | `ConnectError: getaddrinfo failed` | pipeline 配置文件需从 HF 下载 | 设 `HF_ENDPOINT` 后再首次加载；之后用缓存 |
| 模型加载太慢 | 前台卡住无输出 | CPU 加载 4GB 模型需 30-60 秒 | GPU 加载只需几秒；等就行 |
| SD 1.5 生二次元质量差 | 画面偏写实/3D | SD 1.5 是写实模型 | 换用 Deliberate v2 等通用模型；或加 CFG 9-12 + 风格锚点 |
| 破解版 PS COM 不可用 | `pywintypes.com_error: 没有注册类` | 破解版跳过了 COM 服务器注册 | 正版 PS 才支持 COM 自动化；破解版走 SAI 文件桥接 |
