import numpy as np

# 1) Un exemple dans train_demo/imgs
img_npz_path = "C:\\Users\\achou\\Desktop\\PFE\\cvpr-sam-on-laptop-2024\\dataset\\train_demo\\imgs\\2D_16P9867M2.npz"
d_img = np.load(img_npz_path, allow_pickle=True)
print("IMG keys:", d_img.keys())
for k in d_img.keys():
    print(" ", k, d_img[k].shape, d_img[k].dtype)

# 2) Le fichier correspondant dans train_demo/gts
gt_npz_path = "C:\\Users\\achou\\Desktop\\PFE\\cvpr-sam-on-laptop-2024\\dataset\\train_demo\\gts\\2D_16P9867M2.npz"
d_gt = np.load(gt_npz_path, allow_pickle=True)
print("GT keys:", d_gt.keys())
for k in d_gt.keys():
    print(" ", k, d_gt[k].shape, d_gt[k].dtype)
