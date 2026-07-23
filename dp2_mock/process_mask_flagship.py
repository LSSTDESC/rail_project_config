import os
import shutil
import pandas as pd
import healpy as hp
import numpy as np

# ── Configuration ────────────────────────────────────────────
INPUT_DIR       = "/global/cfs/cdirs/lsst/groups/PZ/Flagship/dp2_mock_run_flagship_gold/"          
OUTPUT_DIR      = "/global/cfs/cdirs/lsst/groups/PZ/Flagship/dp2_mock_run_flagship_gold/"      
MASK_FILE       = "/global/cfs/cdirs/lsst/groups/PZ/users/qhang/dp2_maps_may/dp2_public_catalog_mask_nside-256.fits"          

COLUMNS_TO_DROP = ["observed_redshift_gal", "ra_mag_gal", "dec_mag_gal", "lsst_u_el_model3_ext", "lsst_g_el_model3_ext", "lsst_r_el_model3_ext" , "lsst_i_el_model3_ext", "lsst_z_el_model3_ext", "lsst_y_el_model3_ext", "euclid_nisp_h_el_model3_ext", "euclid_nisp_j_el_model3_ext", "euclid_nisp_y_el_model3_ext", "euclid_vis_el_model3_ext"]       

COLUMNS_TO_RENAME = {}

NSIDE = 256
# ─────────────────────────────────────────────────────────────


# Load the healpix mask once
mask = hp.read_map(MASK_FILE)

# Get all parquet files, walking through {pixel} subfolders
parquet_files = []
for pixel_folder in os.listdir(INPUT_DIR):
    pixel_path = os.path.join(INPUT_DIR, pixel_folder)
    parquet_path = os.path.join(pixel_path, "part-0.pq")
    if os.path.isdir(pixel_path) and os.path.exists(parquet_path):
        parquet_files.append((pixel_folder, parquet_path))

print(f"Found {len(parquet_files)} parquet files")

for pixel_folder, input_path in parquet_files:
    print(f"Processing pixel: {pixel_folder}")

    # 1. Read
    df = pd.read_parquet(input_path)

    # 2. Drop columns (only if they exist, avoids errors)
    df = df.drop(columns=[c for c in COLUMNS_TO_DROP if c in df.columns])

    # 3. Rename columns
    #df = df.rename(columns=COLUMNS_TO_RENAME)

    # 4. Convert ra/dec to healpix pixel indices
    pixel_ids = hp.ang2pix(NSIDE, df['ra'], df['dec'], lonlat=True)

    # 5. Apply mask
    in_mask = mask[pixel_ids] == 1
    df = df[in_mask]

    # 6. If table is empty, delete the file and its parent folder
    if len(df) == 0:
        print("Pixel empty, deleted.")
        pixel_dir = os.path.join(INPUT_DIR, pixel_folder)
        shutil.rmtree(pixel_dir)        # deletes the folder and everything inside it
        print(f"  → Empty after mask cut — deleted folder: {pixel_dir}")
        continue                        # skip to next file

    # 7. Save non-empty table
    output_pixel_dir = os.path.join(OUTPUT_DIR, pixel_folder)
    os.makedirs(output_pixel_dir, exist_ok=True)
    output_path = os.path.join(output_pixel_dir, "part-0.pq")
    df.to_parquet(output_path, index=False)
    print(f"  → Saved {len(df)} rows to {output_path}")

print("Done!")
