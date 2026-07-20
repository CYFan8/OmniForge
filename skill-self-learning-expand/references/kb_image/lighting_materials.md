# 光影材质

> 来源: kb002_lighting_materials.md + sd_techniques.md + ai_image_techniques.md

## 三点布光法
- Key Light (主光): 45度侧前方, 最强光源, 塑造立体感
- Fill Light (补光): 另一侧45度, 强度30-50%, 消除过暗阴影
- Rim Light (轮廓光): 后方偏上, 分离主体与背景
- 氛围光: 场景环境反射, 柔和不抢眼

## SD光影关键词
- 黄金时刻: "golden hour, warm sunlight, long shadows, volumetric lighting"
- 阴天柔和: "overcast, soft diffused light, flat lighting"
- 室内暖光: "warm interior lighting, tungsten, cozy atmosphere"
- 霓虹夜景: "neon lights, cyberpunk, rim lighting, dramatic shadows"

## PBR材质参数速查
| 材质 | 金属度 | 粗糙度 | 次表面 | 特性 |
|------|--------|--------|--------|------|
| 抛光金属 | 1.0 | 0.05-0.2 | 0 | 锐利高光, 环境反射 |
| 磨砂金属 | 0.8 | 0.3-0.5 | 0 | 柔和高光, 模糊反射 |
| 玻璃 | 0 | 0-0.05 | 0 | 透射+折射, IOR 1.45 |
| 皮肤 | 0 | 0.4-0.6 | 0.1-0.3 | 漫反射为主, 微弱透光 |
| 布料 | 0 | 0.6-0.9 | 0 | 几乎无高光, 纤维感 |

## 光影常见缺陷
- 光源方向混乱: 同一画面出现互斥的阴影方向
- 金属过曝: 反射太强失去材质纹理
- 皮肤塑料感: 缺少SSS次表面散射
- 色温不统一: 窗外冷光+室内暖光没做色彩调和
