import os
from PIL import Image

PATCH_SIZE = 256

BASE_DIR = r"C:\Users\achou\Desktop\PFE\Image_Segmentation\DATASET_R2U-net"
SRC_DATASET = r"C:\Users\achou\Desktop\PFE\Image_Segmentation\DATASET_R2U-net\dataset_catégorie2"          # dataset d'origine
DST_DATASET = r"C:\Users\achou\Desktop\PFE\Image_Segmentation\DATASET_R2U-net\dataset_categorie2_patches"  # nouveau dataset (sans accent)

def make_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def crop_image_and_mask(img_path, mask_path, out_img_dir, out_mask_dir, base_name):
    img = Image.open(img_path).convert("RGB")
    mask = Image.open(mask_path).convert("L")

    if img.size != mask.size:
        print(f"SKIP SIZE MISMATCH: {img_path} {img.size} {mask.size}")
        return

    width, height = img.size
    patch_id = 0

    for y in range(0, height - PATCH_SIZE + 1, PATCH_SIZE):
        for x in range(0, width - PATCH_SIZE + 1, PATCH_SIZE):
            img_patch = img.crop((x, y, x + PATCH_SIZE, y + PATCH_SIZE))
            mask_patch = mask.crop((x, y, x + PATCH_SIZE, y + PATCH_SIZE))

            patch_name = f"{base_name}_x{x}_y{y}_p{patch_id}"
            img_out_path = os.path.join(out_img_dir, patch_name + ".png")
            mask_out_path = os.path.join(out_mask_dir, patch_name + "_segmentation.png")

            img_patch.save(img_out_path)
            mask_patch.save(mask_out_path)

            patch_id += 1

    if patch_id == 0:
        print(f"NO PATCHES (too small): {img_path}")

def process_split(split_name):
    # ex : split_name = 'train' -> train, train_GT
    src_img_dir = os.path.join(BASE_DIR, SRC_DATASET, split_name)
    src_mask_dir = os.path.join(BASE_DIR, SRC_DATASET, split_name + "_GT")

    dst_img_dir = os.path.join(BASE_DIR, DST_DATASET, split_name)
    dst_mask_dir = os.path.join(BASE_DIR, DST_DATASET, split_name + "_GT")

    make_dirs(dst_img_dir)
    make_dirs(dst_mask_dir)

    img_files = [f for f in os.listdir(src_img_dir)
                 if f.lower().endswith((".jpg", ".png", ".jpeg", ".tif"))]

    for f in img_files:
        # 16P10748M1.jpg -> 16P10748M1_segmentation.png
        name, ext = os.path.splitext(f)
        img_path = os.path.join(src_img_dir, f)
        mask_name = name + "_segmentation.png"
        mask_path = os.path.join(src_mask_dir, mask_name)

        if not os.path.exists(mask_path):
            print(f"MASK NOT FOUND for {img_path} -> {mask_path}")
            continue

        base_name = name
        crop_image_and_mask(img_path, mask_path, dst_img_dir, dst_mask_dir, base_name)

        print(f"Processed {img_path}")

if __name__ == "__main__":
    for split in ["train", "val", "test"]:
        print(f"=== Processing {split} ===")
        process_split(split)
    print("Done.")
