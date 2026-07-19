---
name: skill-finder
description: >-
  技能发现与安装器。当你想发现、搜索、安装新技能时使用。
  可以列出所有已安装技能、从多个来源搜索技能关键词、
  安装来自 D 盘技能库或 GitHub 仓库的技能。
  替代手动搜索 skill-installer 的用法，提供统一发现入口。
---

# Skill Finder — 技能发现与安装器

## 工作流

```
用户说「找个能 X 的技能」
    │
    ▼
① 列出本地已安装的所有技能（~/.codex/skills/）
    │
    ▼
② 搜索 D:i_skill_lib\ 中的可用技能
    │
    ▼
③ 可选：搜索 GitHub 来源（openai/skills 等）
    │
    ▼
④ 匹配用户需求 → 推荐最佳技能
    │
    ▼
⑤ 如果未安装 → 自动调用 skill-installer 安装
    │
    ▼
⑥ 告知用户技能位置和功能
```

---

## 技能来源

| 来源 | 路径 | 优先级 |
|------|------|--------|
| 本地已安装 | ~\.codex\skills\ | 已就绪，立即可用 |
| 本地技能库 | D:i_skill_lib\ | 部署后才可用 |
| GitHub 官方仓库 | openai/skills | 需安装 |
| 任意 GitHub 仓库 | 用户提供 URL | 需安装 |

---

## 使用方式

### 列出所有技能

当用户想知道「有哪些技能」时，列出：

1. **本地已安装** — 直接列出 ~\.codex\skills\ 下所有目录
2. **D 盘技能库** — 列出 D:i_skill_lib\ 中尚未部署的技能
3. **标记状态** — [已安装] / [需部署] / [来自 GitHub]

### 搜索技能

当用户说「找个能 X 的技能」时：

1. 先用关键词匹配已安装技能的 description
2. 再搜 D 盘技能库
3. 可选搜 GitHub openai/skills
4. 给出匹配度最高的推荐

### 安装技能

如果推荐技能未安装：

1. 本地库未部署 → 复制到 ~\.codex\skills2. GitHub 来源 → 调用 skill-installer 的脚本安装

---

## 实现

### 辅助脚本：scripts/find_skills.py

```python
# 用法示例
python find_skills.py list           # 列出所有已安装技能
python find_skills.py search 数学     # 按关键词搜索
python find_skills.py sources        # 列出所有可用来源
python find_skills.py install 名称   # 安装指定技能
```

---

## 相关资源

- 技能安装底层由 skill-installer 提供
- 本地技能库仓库：D:i_skill_lib- 官方技能源：https://github.com/openai/skills
