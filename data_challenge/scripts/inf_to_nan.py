import glob
import tables_io
import numpy as np


files = glob.glob("/global/cfs/cdirs/lsst/groups/PZ/data/*/pz_challenge_taskset_*.hdf5")

for f in files:
    tt = tables_io.read(f)

    tt_out = {}
    for k, v in tt.items():
        tt_out[k] = np.where(np.isinf(v), np.nan, v)

    print(f)
    tables_io.write(tt_out, f)

