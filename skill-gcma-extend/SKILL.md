---
name: skill-gcma-extend
description: >-
  GCMA（Generative Contextual Memory Architecture）记忆系统高阶拓展。
  当需要进行记忆时间旅行、自定义压缩策略、记忆评分器调优、
  双时态分片管理、记忆账本审计、归档恢复等高级操作时自动激活。
  包含：时间旅行查询、自定义压缩评分器、双时态分片操作、
  派生视图重建、记忆核算。
---

# GCMA 记忆系统高阶拓展

本 Skill 提供 GCMA 四层记忆体系的高级操作指南。

---

## 一、GCMA 四层体系回顾

| 层级 | 名称 | 温度 | 特征 |
|------|------|------|------|
| L4 | 滑动窗口 | 热 | 当前会话上下文，实时变化 |
| L3 | 对话摘要 | 温 | 每轮对话的结构化摘要 |
| L2 | 用户画像 | 凉 | 用户偏好、习惯、知识水平的长期画像 |
| L1 | 会话元数据 | 冷 | 时间戳、token消耗、会话统计 |

### 策略引擎组件


---

## 二、时间旅行查询

时间旅行允许回溯历史状态。语法：

### 基础查询

`
@L4(2026-07-15)          → 查看某日 L4 快照
@L3(session:abc123)      → 查看特定会话的 L3 摘要
@L2(before:2026-07-01)   → 查看此日期前的 L2 画像状态
@L1(range:[2026-06, 2026-07]) → L1 元数据范围查询
`

### 状态对比

`
@diff(L4, 2026-07-14, 2026-07-15)  → 两天 L4 状态差异
@diff(L2, before, after)            → 用户画像变化
`

### 归档恢复

`
@archive(find:"关键词")              → 在归档中搜索
@archive(restore:id)                 → 从归档恢复到当前层
@archive(list)                       → 列出所有归档条目
`

---

## 三、自定义压缩策略

### 压缩评分器

记忆压缩的评分公式：

`
score = w1 × recency + w2 × relevance + w3 × richness + w4 × frequency

recency   = exp(-λ × Δt)          # 时间衰减
relevance = cosine(query, memory)  # 与当前任务的相关性
richness  = len(details) / max     # 信息密度
frequency = n / total              # 被引用的频率
`

#### 默认权重

| 维度 | 默认 w | 说明 |
|------|--------|------|
| recency | 0.35 | 新近度，近期信息权重更高 |
| relevance | 0.30 | 与当前上下文的相关性 |
| richness | 0.20 | 信息丰富度 |
| frequency | 0.15 | 历史引用频率 |

#### 自定义权重

`
@compression(weights: {recency:0.4, relevance:0.4, richness:0.1, frequency:0.1})
`

### 压缩触发条件


### 压缩结果格式

`json
{
  "compressed_from": "L4",
  "compressed_to": "L3",
  "entries_before": 15,
  "entries_after": 3,
  "compression_ratio": "5:1",
  "dropped": ["低价值条目清单"],
  "preserved": ["高价值摘要"]
}
`

---

## 四、双时态分片操作

### Content Time（事件时间）

记忆中的事件实际发生的时间。

`
@ct("2026-07-15T14:30:00+08:00")  → 查询某个事件时间的记忆
@ct(range:[2026-07-01, 2026-07-15]) → 时间范围查询
`

### Record Time（系统时间）

记忆被系统记录的时间。

`
@rt("2026-07-15T14:35:00+08:00")  → 查询某个记录时间的记忆
@rt(after: "2026-07-15T14:00")    → 此时间之后记录的记忆
`

### 分片状态

| 状态 | 含义 | 操作 |
|------|------|------|
| Empty | 无数据 | 初始化分片 |
| Active | 活跃中可读写 | 正常查询/写入 |
| Archived | 已归档只读 | 仅时间旅行可查询 |

### 分片操作

`
@slice(ct:2026-07, create)        → 新建7月分片
@slice(ct:2026-06, archive)       → 归档6月分片
@slice(ct:2026-05, purge)         → 清除5月分片（谨慎！）
@slice(list)                      → 列出所有分片状态
`

---

## 五、记忆账本（Memory Ledger）

### 账本结构


### 账本操作

`
@ledger(verify)                    → 验证链式完整性
@ledger(entry:id)                  → 查看单条记录
@ledger(trace:content_hash)        → 溯源某条内容的完整历史
@ledger(stats)                     → 账本统计（条目数/链长/大小）
`

### 派生视图

从账本惰性重建的可丢弃缓存：

`
@view(create:"user_profile")       → 从账本重建L2用户画像视图
@view(refresh:"user_profile")      → 刷新视图
@view(drop:"user_profile")         → 丢弃视图（下次查询自动重建）
@view(list)                        → 列出所有派生视图
`

---

## 六、记忆核算

`
@audit(run)                        → 执行完整记忆审计
@audit(gaps)                       → 查找信息缺口（跨度超过阈值的时间段）
@audit(consistency)                → 检查层级间一致性
@audit(report)                     → 生成审计报告
`

