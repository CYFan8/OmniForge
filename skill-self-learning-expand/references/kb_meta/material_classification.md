# 素材分类算法

> 来源: skill-self-learning-expand 素材归集

## 多模态文件自动归类规则

### 按文件类型一级分类
| 扩展名 | 归类 | 目标分区 |
|--------|------|---------|
| .txt .md .docx .pdf | 文本素材 | kb_script |
| .png .jpg .psd .tiff .exr | 图像素材 | kb_image |
| .blend .fbx .obj .gltf | 3D资产 | kb_blender |
| .json .yaml .toml .cfg | 配置/元数据 | kb_meta |

### 按内容语义二级分类
- 扫描文件内容关键词 -> 语义向量匹配 -> 分入最接近的知识库分区
- 跨域素材(如同时含剧本+分镜描述的文档): 分配到主域分区, 副域加交叉索引
- 新拓展包的素材: 创建新分区 + 注册新标签 + 更新分类模型

### 切片粒度标准
- 剧本: 按场景/场次切分 (~500-1000字/片)
- 生图: 按分镜/角色切分 (1张图+关联提示词为1片)
- 建模: 按资产切分 (1个.blend文件+关联参考图为1片)
- 元数据: 按配置项切分 (1个配置区块为1片)

### 向量化入库
- Embedding模型: sentence-transformers (复用skill-system-core)
- 索引格式: chunk_id -> embedding_vector -> partition_tag
- 检索时: query -> embedding -> 分区内相似度排序 -> Top-K返回
