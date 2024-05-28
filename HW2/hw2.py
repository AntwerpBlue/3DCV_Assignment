import torch
from pytorch3d.io import load_obj,save_obj

verts_flame, faces_flame, aux = load_obj("data/flame_model.obj")
verts_head, faces_head, axu = load_obj("data/head_model.obj")