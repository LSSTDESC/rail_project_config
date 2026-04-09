import glob
import os
import tables_io

res_dir = '/global/cfs/cdirs/lsst/groups/PZ/data/reserved/'
pub_dir = res_dir.replace('reserved', 'public')

files = glob.glob(f"{res_dir}/*.hdf5")


for f in files:
    basename = os.path.basename(f)
    tt = tables_io.read(f)
    tt.pop('redshift')

    outfile = os.path.join(pub_dir, basename)

    print(outfile)
    tables_io.write(tt, outfile)

