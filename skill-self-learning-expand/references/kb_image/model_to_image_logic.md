# 建模前置生图逻辑

> 来源: skill-image-generation Model-to-Image + Blender三渲二管线

## 核心原则: 锁定3D结构
Model-to-Image的核心目标是在3D模型已有正确结构的基础上优化材质和光影, 而非重新生成内容。

## 工作流
1. Blender渲染 -> 输出: 线稿(Wireframe) + 灰度底图(Grayscale) + 法线图(Normal)
2. SD img2img -> 输入: 灰度底图 + 线稿引导
3. 去噪强度: 0.3-0.5 (保留原结构, 仅叠加材质光影)
4. ControlNet: Canny边缘检测 (结构锁死) + Depth深度图

## 关键参数
- Denoising Strength: 0.35 (结构保留>80%)
- CFG Scale: 7-8.5 (不过度偏离原图)
- ControlNet权重: 0.8-1.0 (Canny + Depth双控)
- 分辨率: 与Blender渲染输出一致

## 降级兜底规则
生图效果差(画面崩坏/结构变形)时自动切换:
1. 降低Denoising -> 0.2, 仅做微调
2. 切换模型 -> Deliberate v2 (写实向)
3. 最终兜底 -> 纯Blender渲染, 不使用AI叠加

## 适用场景
- 基础3D模型材质不足 -> SD叠加PBR纹理
- 三渲二线稿需要写实化 -> SD叠加光影层次
- 低模需要细节增强 -> SD叠加normal细节

## 不适用场景 (禁止)
- 结构本身有透视问题 -> 先修Blender模型
- 需要改变物体形状 -> 不改模型直接SD会崩
- 角色肢体/手指 -> 极易变形, 禁用
