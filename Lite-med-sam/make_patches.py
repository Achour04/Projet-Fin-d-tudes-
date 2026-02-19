import os
from pathlib import Path
import numpy as np

PATCH_SIZE = 256
STRIDE = 256   # ou < 256 si tu veux du recouvrement

def extract_patches(img, mask, base_name, split, out_root):
    H, W = img.shape[:2]
    patch_id = 0
    out_imgs = Path(out_root) / f"{split}_patches" / "imgs"
    out_gts  = Path(out_root) / f"{split}_patches" / "gts"
    out_imgs.mkdir(parents=True, exist_ok=True)
    out_gts.mkdir(parents=True, exist_ok=True)

    for y in range(0, H - PATCH_SIZE + 1, STRIDE):
        for x in range(0, W - PATCH_SIZE + 1, STRIDE):
            img_patch = img[y:y+PATCH_SIZE, x:x+PATCH_SIZE, :]
            gt_patch  = mask[y:y+PATCH_SIZE, x:x+PATCH_SIZE]

            if np.all(gt_patch == 0):
                continue

            patch_name = f"{base_name}_y{y}_x{x}_{patch_id}.npz"
            box = np.array([[0, 0, PATCH_SIZE, PATCH_SIZE]], dtype=np.int64)

            np.savez_compressed(
                out_imgs / patch_name,
                imgs=img_patch,
                boxes=box
            )
            np.savez_compressed(
                out_gts / patch_name,
                gts=gt_patch
            )
            patch_id += 1

    print(f"{base_name}: {patch_id} patches sauvegardés.")

def process_split(split):
    root = Path("dataset") / f"{split}_demo"
    imgs_dir = root / "imgs"
    gts_dir  = root / "gts"

    print(f"\n=== Split: {split} ===")
    print("imgs_dir:", imgs_dir)
    print("gts_dir :", gts_dir)

    out_root = Path("dataset")
    npz_files = sorted(imgs_dir.glob("*.npz"))
    print("Nb de fichiers trouvés:", len(npz_files))

    for f in npz_files:
        base = f.stem
        print("  ->", base)
        img_npz = np.load(f, allow_pickle=True)
        gt_npz  = np.load(gts_dir / f"{base}.npz", allow_pickle=True)

        img = img_npz["imgs"]
        gts = gt_npz["gts"]

        extract_patches(img, gts, base, split, out_root)

if __name__ == "__main__":
    for split in ["train", "val"]:
        process_split(split)
