# 三渲二分层渲染(NPR)

> 来源: skill-blender-modeling 渲染引擎 + 三渲二NPR渲染工艺

## NPR vs PBR
- PBR(物理渲染): 模拟真实光照, Cycles, 写实向
- NPR(非真实渲染): 模拟手绘/动画风格, Eevee+Compositor, 二次元向
- 三渲二: 3D模型 -> 2D动画风格的渲染管线

## 分层渲染输出
1. 线稿层(Freestyle/Line Art): 物体边缘+内部结构线
2. 二分色层(Toon Shader): 亮部/暗部纯色, 无渐变
3. 高光层(Specular Toon): 锐利高光区域
4. 阴影层(Shadow): 软阴影/硬阴影
5. AO层(Ambient Occlusion): 凹陷区域暗部增强
6. 深度层(Z-Depth): 用于后期景深合成

## Blender NPR设置
- 渲染引擎: Eevee (实时NPR)
- 着色器: Diffuse BSDF -> Shader to RGB -> Color Ramp(Constant)
- 线稿: View Layer Properties -> Freestyle 或 Grease Pencil Line Art
- 输出格式: EXR多层 或 PNG序列(每层独立文件)

## 输出供给生图模块的规范
- 线稿层: 纯黑白, 线条清晰无断裂
- 二分色: 明暗对比明确, 无中间灰色
- 分辨率: 1920x1080 或与最终成片一致
- 文件命名: layer_wireframe.png / layer_toon.png / layer_shadow.png

## 光影失真常见缺陷
- 线稿断续: Freestyle参数过严, 放宽角度阈值
- 二分色中间灰: Color Ramp的Constant模式未开启
- 阴影方向错误: 光源位置与主光Key Light不一致
- 人物与场景光影不统一: 检查所有材质是否使用相同光源组

## 三渲二质量自检
- [ ] 线稿完整, 无断裂
- [ ] 明暗二分清晰, 无渐变
- [ ] 光源方向统一(全程单一主光源)
- [ ] 人物与场景光影风格一致
- [ ] 输出图层完整(至少线稿+二分色+阴影三层)
