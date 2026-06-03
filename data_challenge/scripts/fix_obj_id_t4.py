import glob
import tables_io
import numpy as np


#files = glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/*/pz_challenge_taskset_*.hdf5")
files = glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/pz_challenge_*_deep_*_blended/35a/output_error_model*.pq")
files += glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/pz_challenge_*_deep_*_blended/35a/output_select*.pq")
files += glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/pz_challenge_*_deep_*_blended/35a/output_unrec*.pq")
files += glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/pz_challenge_*_deep_*_blended/35a/output_dered*.pq")

files += glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/pz_challenge_*_deep_*_blended/35b/output_error_model*.pq")
files += glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/pz_challenge_*_deep_*_blended/35b/output_select*.pq")
files += glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/pz_challenge_*_deep_*_blended/35b/output_unrec*.pq")
files += glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/pz_challenge_*_deep_*_blended/35b/output_dered*.pq")

for f in files:
    tt = tables_io.read(f)
    
    for k, v in tt.items():
        tt[k] = np.where(np.isinf(v), np.nan, v)
    tt['object_id'] = (10_000_000*tt['hpx_idx'] + tt['group_id']).to_numpy().astype(int)
    
    print(f)
    tables_io.write(tt, f)

