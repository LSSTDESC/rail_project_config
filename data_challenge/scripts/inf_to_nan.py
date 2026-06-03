import tables_io
import numpy as np
import sys


def inf_to_nan(files):

    for f in files:
        tt = tables_io.read(f)

        tt_out = {}
        for k, v in tt.items():
            tt_out[k] = np.where(np.isinf(v), np.nan, v)

        print(f)
        tables_io.write(tt_out, f)


if __name__ == '__main__':

    files = sys.argv[1:]
    inf_to_nan(files)

    
