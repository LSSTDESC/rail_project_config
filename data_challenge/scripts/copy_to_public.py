from pathlib import Path
import os
import sys
import tables_io

BASE_AREA = Path(os.environ['PZ_DATA_AREA'])
res_dir = BASE_AREA / 'reserved'
pub_dir = BASE_AREA / 'public'


def copy_files(files: list[str]) -> None:

    for f in files:
        basename = os.path.basename(f)
        tt = tables_io.read(f)
        tt.pop('redshift')
        
        outfile = os.path.join(pub_dir, basename)
        
        print(outfile)
        tables_io.write(tt, outfile)


if __name__ == '__main__':

    files = sys.argv[1:]
    copy_files(files)

    
