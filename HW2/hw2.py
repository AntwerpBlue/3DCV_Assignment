import torch
from pytorch3d.io import load_obj,save_obj

verts_flame, faces_flame, aux = load_obj("data/flame_model.obj")
verts_head, faces_head, axu = load_obj("data/head_model.obj")

mean_pos_flame=torch.mean(verts_flame,0)
mean_pos_head=torch.mean(verts_head,0)
trans=mean_pos_head-mean_pos_flame
verts_flame=verts_flame+trans

save_obj("data/flame_model_trans.obj", verts=verts_flame, faces=faces_flame[0])
