---
name: skill-code-review
description: >-
  四阶段代码工程闭环：生成代码 → 自检 → 自我完善 → 自我学习沉淀。
  适用于任何代码编写任务，确保输出质量持续提升、经验不断积累。
  当用户要求写代码、实现功能、修复 Bug、重构代码时自动激活。
  包含：代码审查清单（P0-P3四级）、自检报告格式、修复优先级、
  学习沉淀机制、数学建模方法代码库、基于Pillow的图像编辑工具。
---

# Code Engineer Loop — 生成 + 自检 + 完善 + 学习

核心哲学：不要只写代码，要为每次写代码积累经验。

`
  +-----------------------------------------------------------+
  |                                                           |
  |   1. 生成代码 (Generate)                                   |
  |      |                                                    |
  |      v                                                    |
  |   2. 自检 (Check) ---- 不通过 ----> 3. 自我完善            |
  |      | 通过                      ^         (Improve)      |
  |      v                           +------------------------+
  |   4. 自我学习 (Learn)                                      |
  |      |                                                    |
  |      v                                                    |
  |   回到 1 或结束                                            |
  |                                                           |
  +-----------------------------------------------------------+
`

---

## 阶段一：生成代码 (Generate)

1. 理解需求：先复述需求确认理解正确
2. 设计方案：输出简要方案(架构/接口/数据流)，请用户确认后再编码
3. 增量实现：一次只实现一个模块，完成后即进入自检阶段

### 输出规范


---

## 阶段二：自检 (Check)

每次生成代码后，必须先自检再交付。

### [P0] 编译/语法检查
- [ ] 代码无语法错误
- [ ] 类型检查通过
- [ ] 导入/依赖无缺失

### [P1] 正确性检查
- [ ] 单元测试全部通过
- [ ] 边界条件已覆盖（空值/极值/异常输入）
- [ ] 核心逻辑可以用一句话说清

### [P2] 质量检查
- [ ] 无硬编码（魔法数字/字符串常量已提取）
- [ ] 错误处理完备
- [ ] 日志/调试输出已移除或转为正式日志
- [ ] 函数长度 < 50 行，单个文件 < 500 行
- [ ] 命名符合项目规范

### [P3] 安全检查
- [ ] 无 SQL 注入风险
- [ ] 无命令注入风险
- [ ] 敏感信息不在代码中硬编码

### 自检报告输出格式

`
## 自检报告

| 等级 | 状态 | 项数 |
|------|------|------|
| P0   | 通过/失败 | 3/3  |
| P1   | 通过/失败 | 3/3  |

结论: 全部通过 / 存在 N 项待修复
`

- 全部通过 → 进入阶段四
- 存在未通过项 → 进入阶段三

---

## 阶段三：自我完善 (Improve)

### 修复优先级

`
P0 编译错误 → P1 正确性 → P2 质量 → P3 安全
   最高          高         中         高
`

### 修复流程

1. 定位 → 2. 诊断根因 → 3. 修复 → 4. 重新检查 → 5. 回归测试

---

## 阶段四：自我学习 (Learn)

### 4.1 更新 CLAUDE.md

追加经验到项目根目录的 CLAUDE.md：

`markdown
## 经验记录 (自动沉淀)
### YYYY-MM-DD: [任务简述]
- 问题: [踩到的坑]
- 原因: [根因分析]
- 方案: [最终方案]
- 下次建议: [直接怎么做]
`

### 4.2 沉淀 Skill

发现可跨项目复用的通用知识时，在 .claude/skills/ 下创建 Skill。

### 4.3 学习日志

在 .claude/learn.log 追加一行：
`
YYYY-MM-DD HH:MM | <任务类型> | <模块> | <关键经验>
`

### 什么值得学

| 应沉淀 | 不该沉淀 |
|--------|---------|
| 踩了 30 分钟以上的 Bug | 显而易见的语法修正 |
| 非显而易见的配置坑 | 拼写错误 |
| 项目特有的约定和模式 | 标准 API 使用 |
| 跨模块的架构决策 | 单行调整 |
| 性能优化经验 | 格式化调整 |

---

## 数学建模方法代码库

优先引用以下实现，避免重复造轮子。

| 模块 | 函数 | 用途 |
|------|------|------|
| 图论 | fs_shortest_path, dijkstra, loyd_warshall | 最短路径/全源距离 |
| DP | knapsack_01, edit_distance | 背包/序列比对 |
| 蒙特卡洛 | monte_carlo_simulate, latin_hypercube_sample | 模拟/降方差 |
| 回归 | linear_regression, multiple_linear_regression | 一元/多元回归 |
| 灰色预测 | gm11_predict | GM(1,1)小样本预测 |
| 评价 | hp_weight, 	opsis, entropy_weight | AHP/TOPSIS/熵权法 |
| 博弈 | 
ash_equilibrium_2x2 | 2人纳什均衡 |
| 时间序列 | exponential_smoothing | 指数平滑预测 |

---

## Pillow 图像编辑工具

用于数学建模中在题目地图/示意图上绘制路线、标注节点、添加文字。

### 基础框架

`python
from PIL import Image, ImageDraw, ImageFont
img = Image.open("原图.png")
draw = ImageDraw.Draw(img)
# ... 修改操作 ...
img.save("修改后.png")
`

### 常用操作

`python
# 直线: 起点→终点, 颜色RGB, 线宽
draw.line(xy=[(100,200),(500,200)], fill=(255,0,0), width=3)

# 矩形: 空心(outline)或填充(fill)
draw.rectangle(xy=[(50,50),(300,200)], outline=(0,0,255), width=2)
draw.rectangle(xy=[(50,250),(300,400)], fill=(0,255,0,128))

# 椭圆: 外接矩形坐标
draw.ellipse(xy=[(100,100),(300,300)], outline=(255,0,0), width=2)

# 多边形
draw.polygon(xy=[(200,100),(100,300),(300,300)], fill=(128,128,128))

# 文字
font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", size=24)
draw.text(xy=(100,50), text="起点S", fill=(0,0,0), font=font)

# 带箭头标注线
import math
def draw_arrow(draw, start, end, color=(255,0,0), width=2, arrow_size=10):
    draw.line([start, end], fill=color, width=width)
    angle = math.atan2(end[1]-start[1], end[0]-start[0])
    p1 = (end[0]-arrow_size*math.cos(angle-math.pi/6), end[1]-arrow_size*math.sin(angle-math.pi/6))
    p2 = (end[0]-arrow_size*math.cos(angle+math.pi/6), end[1]-arrow_size*math.sin(angle+math.pi/6))
    draw.polygon([end, p1, p2], fill=color)
`

### 注意事项
- PNG透明图用 img.convert("RGBA")
- 大尺寸图用 numpy 加速像素遍历
- 字体加载失败用 ImageFont.load_default()
- 坐标均为整数像素

