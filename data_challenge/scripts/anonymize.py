import tables_io
import numpy as np
import sys

def anonymize(files: list[str]):

    count = 0
    for f in files:
        tt = tables_io.read(f)
        n_obj = len(tt['object_id'])
        tt['object_id'] = np.arange(count, count+n_obj)
        count += n_obj
        print(f)
        tables_io.write(tt, f)


if __name__ == '__main__':

    files = sys.argv[1:]
    anonymize(files)

        
