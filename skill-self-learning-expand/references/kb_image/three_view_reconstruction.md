# 三视图结构还原

> 来源: skill-image-generation 三视图重建 + Blender建模导入需求

## 三视图标准
- 正面(Front): 展示五官对称、身体比例、服装正面细节
- 侧面(Side): 展示身体厚度、鼻子/耳朵轮廓、后背曲线
- 背面(Back): 展示后背服装、发型后面、装备细节

## SD生图要点
- 提示词模板: "character turnaround sheet, front view side view back view, three views, orthographic, reference sheet, white background"
- 负向: "perspective, foreshortening, dynamic pose, angled view"
- 分辨率: 建议1024x512 (横三连) 或 512x1024 (竖三连)

## 三视图质量标准
1. 三视图间比例一致: 头大小/肩宽/身高完全相同
2. 服装细节对应: 正面口袋位置=侧面可见=背面有对应
3. 光线统一: 三视图采用相同光照(通常正面漫射光)
4. 正交投影: 无透视变形, 边线平行

## 尺寸标注规范
- 总高: 头顶->脚底 (cm)
- 肩宽: 左肩峰->右肩峰
- 头身比: 头部长度:总高
- 关键节点: 腰线/膝盖/手腕位置标注

## 供给Blender建模的转换规则
- 三视图对齐: Front->XZ平面 / Side->YZ平面 / Back->XZ平面(反)
- 比例锁定: 三视图导入后Scale一致
- 参考透明度: 0.5-0.7, 不遮挡建模视线
