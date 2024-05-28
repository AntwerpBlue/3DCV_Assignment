import torch
from pytorch3d.io import save_obj

# 构建四面体的顶点坐标
vertices = torch.zeros((4, 3), dtype=torch.float32) ###构建一个(4,3)的二维zero tensor
vertices[0] = torch.tensor([0.0, 1.0, 0.0]) ### 类似C语言从0开始索引，对应V1的XYZ坐标
# FILL: 更新另外三个点，可自行设置坐标，合理即可
vertices[1] = ...
vertices[2] = ...
vertices[3] = ...

# 构建四面体的面片索引
faces = torch.zeros((4,3), dtype=torch.int64)
faces[0] = torch.tensor([0, 1, 2]) ### 这里对应（v1,v2,v3）三角形包含的顶点的index, 按右手系拇指朝外顺序
# FILL: 更新另外三个面片所包含顶点的index
faces[1] = ...
faces[2] = ...
faces[3] = ...

# 保存网格
save_obj("tetrahedron.obj", vertices, faces)