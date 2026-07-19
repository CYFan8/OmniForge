# AI Image Generation Complete Techniques

Sources: web tutorials + 1M+ anime images analysis + real testing

## Anime Style (SD 1.5 base model)

### Prompt Formula
masterpiece, best quality, anime style, illustration,
[character], [outfit], [expression], [pose],
[style anchor], [artist ref], [color palette],
clean lines, cel shaded, 2d art, vibrant colors

### Style Anchors
Studio Ghibli: studio ghibli style, hayao miyazaki, soft watercolor
Shinkai: makoto shinkai, vibrant sky, lens flare, detailed bg
Cyberpunk: cyberpunk anime, akira style, 90s anime, neon, dark
Slice of life: kyoani style, soft lighting, school setting
Action: dynamic pose, speed lines, impact frames
Healing: iyashikei, pastel colors, soft shading, gentle

### Negative Prompt (Anime)
3d, realistic, photorealistic, photograph, bad anatomy,
bad hands, extra fingers, fused fingers, ugly, deformed,
blurry, jpeg artifacts, signature, watermark, text,
western art style, oil painting, thick lines

### Best Params (Anime)
CFG: 9-12 | Steps: 35-50 | Resolution: 512x768

---

## Photorealistic Style

### Prompt Formula
masterpiece, best quality, 8k, photorealistic,
[subject], [environment], [lighting],
national geographic style, professional photography,
sharp focus, highly detailed, intricate

### Lighting Keywords
Golden hour: golden hour, warm sunset, rim lighting
Overcast: soft diffused light, cloudy, moody
Neon: neon lighting, cyberpunk, colored rim light
Studio: studio lighting, three point, professional
Backlit: backlit, silhouette, dramatic rim light
Volumetric: volumetric lighting, god rays

### Negative Prompt (Realistic)
worst quality, low quality, bad anatomy, bad hands,
missing fingers, extra fingers, blurry, jpeg artifacts,
signature, watermark, text, ugly, deformed, distorted,
disfigured, poorly drawn, bad proportions, extra limbs,
cloned face, grainy, noisy, oversaturated

---

## Quick Reference

| Style | Steps | CFG | Time | Quality |
|-------|-------|-----|------|--------|
| Fast preview | 15-20 | 7 | 5s | Basic |
| Standard | 30-35 | 7-8 | 10s | Good |
| High quality | 40-50 | 8-9 | 15s | Excellent |
| Anime | 35-50 | 9-12 | 13-18s | Good-A |
| Realistic | 30-45 | 7-8.5 | 10-15s | Good-A |

## Prompt Golden Rules

1. Quality words FIRST (highest weight)
2. Style anchor SECOND
3. Subject description THIRD
4. Details FOURTH
5. Artist/style ref LAST

Single subject: add "a single, solo, clean background, isolated"
Negative: add "multiple subjects, crowd, group, background clutter"

## Common Fixes

| Problem | Fix |
|---------|-----|
| Anime looks 3D | CFG to 10+, add cel shaded, flat color |
| Realistic looks animated | CFG to 7-8, add photorealistic, photograph |
| Bad hands | neg: bad hands, extra fingers, fused fingers |
| Too dark | prompt: bright, well lit; lower CFG |
| Cluttered | prompt: simple composition, minimalist, clean |
