---
name: skill-software-dev
description: 综合软件开发能力插件 —— 覆盖全栈开发、前端/后端/移动端/AI/DevOps/架构等52个专业软件开发Agent的索引和路由。当你需要做软件、写代码、搭系统、或解决工程技术问题时激活。
---

# Skill: Software Development（软件开发）

## 调度关键词
- `做软件 / 开发 / 编程 / 写代码 / 搭系统 / 工程技术`

## 用前必读

本 Skill 不是让你把 52 个 Agent 全塞进对话 —— 而是当你遇到具体开发任务时，快速定位最合适的专用 Agent，然后用 `@agent-slug` 加载它。

所有 Engineering Agent 已安装在 `~/.codex/agents/` 中。

---

## Agent 分类索引

### 1. 通用开发 / 架构
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 💎 Senior Developer | `@senior-developer` | 全栈实现，Laravel/Livewire/Three.js 精工开发 |
| ⚡ Rapid Prototyper | `@rapid-prototyper` | 3天出 MVP，快速验证想法 |
| 🏛️ Software Architect | `@software-architect` | 系统架构设计，DDD 领域建模，ADR 决策记录 |
| 🧭 Codebase Onboarding Engineer | `@codebase-onboarding-engineer` | 接手不熟悉的代码库，快速读懂项目 |

### 2. 前端
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 🎨 Frontend Developer | `@frontend-developer` | React/Vue/Angular 前端开发 |
| 🏛️ USWDS Developer | `@uswds-developer` | 美国政府网站，21st Century IDEA 合规 |

### 3. 后端 / API
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 🏗️ Backend Architect | `@backend-architect` | 后端系统设计，微服务，API 开发 |
| 🔌 API Platform Engineer | `@api-platform-engineer` | 公共/合作伙伴 API，OpenAPI/gRPC，SDK 生成 |
| 🔧 Filament Optimization Specialist | `@filament-optimization-specialist` | Filament PHP 后台优化 |

### 4. AI / 机器学习
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 🤖 AI Engineer | `@ai-engineer` | ML 模型开发、部署、生产集成 |
| 🧬 AI Data Remediation Engineer | `@ai-data-remediation-engineer` | 自愈数据管道，自动修复数据异常 |
| 🕸️ Multi-Agent Systems Architect | `@multi-agent-systems-architect` | 多 Agent 协同架构设计 |
| 🧬 Prompt Engineer | `@prompt-engineer` | Prompt 编写 + 系统优化 |

### 5. 移动端
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 📱 Mobile App Builder | `@mobile-app-builder` | Swift/Kotlin/Flutter/React Native 开发 |
| 🚀 Mobile Release Engineer | `@mobile-release-engineer` | App Store / Play Console 发布流程 |
| 💬 WeChat Mini Program Developer | `@wechat-mini-program-developer` | 微信小程序开发 |

### 6. 桌面端
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 💻 Desktop App Engineer | `@desktop-app-engineer` | Electron/Tauri 桌面应用开发 |

### 7. CMS / 网站系统
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 🧱 CMS Developer | `@cms-developer` | Drupal/WordPress 主题 + 插件开发 |
| ⚡ Drupal Performance Engineer | `@drupal-performance-engineer` | Drupal Core Web Vitals 优化 |
| 🛒 Drupal Shopping Cart Engineer | `@drupal-shopping-cart-engineer` | Drupal Commerce 电商 |
| ⚡ WordPress Performance Engineer | `@wordpress-performance-engineer` | WordPress 性能优化 |
| 🛍️ WordPress Shopping Cart Engineer | `@wordpress-shopping-cart-engineer` | WooCommerce 电商 |

### 8. DevOps / 基础设施
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| ⚙️ DevOps Automator | `@devops-automator` | CI/CD，基础设施自动化 |
| 🛡️ SRE | `@sre-site-reliability-engineer` | SLO，可观测性，chaos engineering |
| 🌐 Network Engineer | `@network-engineer` | 网络设备配置，Cisco/Juniper/Palo Alto |
| 🛟 Database Reliability Engineer | `@database-reliability-engineer` | 高可用、备份、迁移、灾备 |
| 💰 FinOps Engineer | `@finops-engineer` | 云成本优化，预留实例，存储优化 |
| ⚡ Autonomous Optimization Architect | `@autonomous-optimization-architect` | API 性能影子测试 + 成本护栏 |

### 9. 数据 / 数据库
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 🔧 Data Engineer | `@data-engineer` | ETL/ELT，Spark，dbt，数据管道 |
| 🗄️ Database Optimizer | `@database-optimizer` | PostgreSQL/MySQL 查优 + 索引策略 |
| 🔎 Search Relevance Engineer | `@search-relevance-engineer` | Elasticsearch/OpenSearch 搜索优化 |
| 📧 Email Intelligence Engineer | `@email-intelligence-engineer` | 邮件数据结构化提取 |

### 10. 安全 / 认证
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 🔐 Identity & Access Engineer | `@identity-access-engineer` | Auth、SSO、RBAC、Clerk/Auth0 |
| 💳 Payments & Billing Engineer | `@payments-billing-engineer` | Stripe/Adyen 支付集成，订阅计费 |
| ⛓️ Solidity Smart Contract Engineer | `@solidity-smart-contract-engineer` | EVM 智能合约，DeFi，Gas 优化 |
| ♿ Section 508 Specialist | `@section-508-accessibility-specialist` | 无障碍合规，VPAT/ACR |

### 11. 开发者体验
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 👁️ Code Reviewer | `@code-reviewer` | 代码审查，正确性+可维护性+安全 |
| 🛠️ Developer Tooling Engineer | `@developer-tooling-engineer` | CLI 工具，内部开发者平台 |
| 🔄 Git Workflow Master | `@git-workflow-master` | Git 工作流，commit 规范，分支策略 |
| 📚 Technical Writer | `@technical-writer` | API 文档、README、教程 |

### 12. 专项领域
| Agent | slug | 什么时候用 |
|-------|------|-----------|
| 🔩 Embedded Firmware Engineer | `@embedded-firmware-engineer` | ESP32、ARM、FreeRTOS 固件开发 |
| 🌐 IoT Fleet Engineer | `@iot-fleet-engineer` | IoT 设备群管理，OTA 升级 |
| 🤝 Realtime Collaboration Engineer | `@realtime-collaboration-engineer` | WebSocket、CRDT、协作文档 |
| 🎬 Video Streaming Engineer | `@video-streaming-engineer` | HLS/DASH 流媒体，ffmpeg 转码 |
| 🎙️ Voice AI Integration Engineer | `@voice-ai-integration-engineer` | 语音转写，Whisper，ASR 集成 |
| 🧩 WebAssembly Engineer | `@webassembly-engineer` | Rust/C++ → Wasm，WASI 运行时 |
| 📜 OrgScript Engineer | `@orgscript-engineer` | OrgScript 语法解析 |
| 🔗 Feishu Integration Developer | `@feishu-integration-developer` | 飞书开放平台集成 |
| 🌍 i18n Engineer | `@i18n-engineer` | 国际化，多语言 |
| 🔪 Minimal Change Engineer | `@minimal-change-engineer` | 手术刀式最小改动 |
| 🚨 Incident Response Commander | `@incident-response-commander` | 事故应急响应 |
| 🖥️ IT Service Manager | `@it-service-manager` | IT 服务管理 |

---

## 快速决策指南

**在 Codex 中做软件时，按这个顺序判断：**

1. **想快速出原型？** → `@rapid-prototyper`
2. **需要设计系统架构？** → `@software-architect`
3. **写具体代码？** → 看技术栈：
   - 前端 → `@frontend-developer`
   - 后端 → `@backend-architect`
   - 移动端 → `@mobile-app-builder`
   - 桌面端 → `@desktop-app-engineer`
   - 全栈通用 → `@senior-developer`
4. **做 AI 功能？** → `@ai-engineer`
5. **搭 CI/CD / 部署？** → `@devops-automator`
6. **数据库设计/优化？** → `@database-optimizer`
7. **代码审查？** → `@code-reviewer`
8. **以上都不对？** → 到上面的分类索引里找对应领域

**在每个 Agent 完成任务后，可以接力给下一个：**
```
@software-architect 设计 → @backend-architect 写后端 → @frontend-developer 写前端 → @devops-automator 部署
```

---

## 关键规则

- 所有 Agent 文件在 `C:\Users\l's'y\.codex\agents\`，slug 就是文件名（不带 .toml）
- 使用方法：`@slug` 激活对应 Agent
- 一个对话中可以串多个 Agent，按阶段接力
- 不需要把所有 Agent 都加载进来，按需加载

## 扩展阅读

- 完整原始 Markdown 文件：`outputs/all-agents-reference/engineering/`
- 其他领域 Agent（Design、Testing、Security 等）见 `~/.codex/agents/`
- 本 Skill 来自 [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
*** End of File
