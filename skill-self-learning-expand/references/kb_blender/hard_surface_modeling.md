# 硬表面建模

> 来源: skill-blender-modeling + Blender 5.1.2 实测

## 核心工作流
1. 参考图导入 -> 对齐三视图(Front/Side/Back)
2. 基础体块搭建 -> Cube/Cylinder + 比例锁定
3. 布尔运算切割 -> 差集(Difference)切细节
4. 倒角(Bevel) -> 消除绝对锐利边, 增加真实感
5. 修改器堆栈 -> Boolean->Remesh->Subdivision

## 布尔运算铁律
- 必须先Apply Scale (Ctrl+A), 否则布尔结果变形
- 布尔后必须加Remesh清理非流形几何
- 修改器顺序: Boolean(切割) -> Remesh(清理) -> Subdivision(平滑)
- 布尔失败常见原因: 法线方向错误、非闭合网格、重叠面

## 拓扑优化原则
- 四边形优先: 避免三角形和N-gon(多于4边的面)
- 边流(Edge Flow): 边缘沿形状自然流动
- 支撑边: 在需要锐利转折处加一圈Loop Cut
- 面数控制: 硬表面低模<10万面, 高模可到50万

## 常用修改器速查
| 修改器 | 用途 | 关键参数 |
|--------|------|---------|
| Mirror | 对称建模 | Axis, Clipping(锁死中线) |
| Subdivision | 平滑表面 | Levels: 视口1-2, 渲染2-3 |
| Solidify | 给平面加厚度 | Thickness, Even Thickness |
| Boolean | 布尔运算 | Difference/Union/Intersect |
| Bevel | 倒角 | Segments: 2-4, Amount |
| Array | 阵列复制 | Count, Relative Offset |

## 常见缺陷
- 非流形几何: 单边共享>2面, 内部面
- 法线翻转: 面朝向不一致导致渲染黑斑
- 布尔破面: 差集后未加Remesh
- 比例失调: 未对齐三视图导致模型走形
