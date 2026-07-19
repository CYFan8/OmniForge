# 贡献指南

## 社区

- 💬 **讨论**: [GitHub Discussions](https://github.com/CYFan8/OmniForge/discussions)
- 🐛 **Bug 反馈**: [Issues](https://github.com/CYFan8/OmniForge/issues)
- 💡 **功能建议**: [Discussions → Ideas](https://github.com/CYFan8/OmniForge/discussions/categories/ideas)

## 如何贡献一个新 Skill

1. **Fork** 本仓库
2. 在根目录创建: `skill-你的技能名/`
3. 写 `SKILL.md`，参考 `skill-system-core/SKILL.md` 格式：

```markdown
---
name: skill-你的技能名
description: >-
  描述这个技能做什么、何时触发。
---

# 技能名

## 功能
简短描述每个功能。

## 依赖清单
| 组件 | 用途 | 安装命令 |
|------|------|---------|

## 踩坑实录
（可选）实机部署中遇到的问题和解决方案。
```

4. 提交 PR，描述你的技能解决了什么问题

## 优化现有 Skill

- 改进 Prompt 质量
- 补充依赖清单
- 追加踩坑实录
- 更新知识库

欢迎任何形式的贡献，哪怕只是改一个错别字。

## 质量标准

- SKILL.md 条目编号清晰
- 每个功能有具体说明
- 标注与其他技能的联动关系
- 依赖清单可执行（复制粘贴就能装）

## 许可

贡献的代码默认使用 MIT 许可。
