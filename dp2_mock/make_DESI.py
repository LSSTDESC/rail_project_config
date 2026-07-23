import pandas as pd
import numpy as np
import healpy as hp
#import matplotlib.pyplot as plt
#import matplotlib
import os

flagship = 1
cardinal = 0

mask_desi = hp.read_map("/pscratch/sd/q/qhang/Flagship/desi-model-mask-nside-256.fits")

if flagship:
    root = '/global/cfs/cdirs/lsst/groups/PZ/Flagship/dp2_mock_run_flagship_gold_test/'
    pixels = os.listdir(root)
    tracers = ["BGS", "LRG", "ELG"]
    # we can grab the mask for BGS, LRG, and ELGs
    for tracer in tracers:
        print(f"Working on {tracer}")
        for pix in pixels:
            fname = root + f"{pix}/output_select_lsst_obs_cond_dp2_DESI_{tracer}_flagship.pq"
            df_desi = pd.read_parquet(fname)
            df_pix = hp.ang2pix(256, df_desi['ra'], df_desi['dec'], lonlat=True)
            ind = np.isin(df_pix, np.arange(len(mask_desi))[mask_desi.astype(bool)])
    
            if pix == pixels[0]:
                df_use = df_desi[ind]
            else:
                df_use = pd.concat([df_use, df_desi[ind]])
        df_use = df_use.reset_index()
        df_use.to_parquet(root + f"output_select_lsst_obs_cond_dp2_DESI_{tracer}_flagship.pq")


if cardinal:
    root1 = "/global/cfs/cdirs/lsst/groups/PZ/Cardinal/parquet_files/dp2_mock_run_cardinal_gold/" 
    # Get all parquet files, walking through {pixel} subfolders
    pixels = os.listdir(root1)
    tracers = ["BGS", "LRG", "ELG_LOP"]
    root = "/global/cfs/cdirs/lsst/groups/PZ/Cardinal/parquet_files/dp2_mock_run_cardinal_gold_test/" 
    for tracer in tracers:
        print(f"Working on {tracer}")
        for pix in pixels:
            fname = root + f"{pix}/output_select_lsst_obs_cond_dp2_DESI_{tracer}_color.pq"
            df_desi = pd.read_parquet(fname)
            df_pix = hp.ang2pix(256, df_desi['ra'], df_desi['dec'], lonlat=True)
            ind = np.isin(df_pix, np.arange(len(mask_desi))[mask_desi.astype(bool)])
    
            if pix == pixels[0]:
                df_use = df_desi[ind]
            else:
                df_use = pd.concat([df_use, df_desi[ind]])
        df_use = df_use.reset_index()
        df_use.to_parquet(root + f"output_select_lsst_obs_cond_dp2_DESI_{tracer}_color.pq")