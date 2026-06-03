import sys
import tables_io
import numpy as np


def null_non_specz(files: list[str]) -> None:
    
    for f in files:
        tt = tables_io.read(f)

        has_specz = np.zeros(len(tt['redshift']), bool)

        for specz in ['DEEP2_LSST', 'DESI_BGS', 'DESI_ELG_LOP', 'DESI_LRG', 'VVDSf02', 'zCOSMOS']:
            if specz in tt:
                has_specz = np.bitwise_or(has_specz.astype(bool), tt[specz].astype(bool))
        tt['redshift'] = np.where(has_specz, tt['redshift'], np.nan)

        print(f)
        tables_io.write(tt, f)


if __name__ == '__main__':

    files = sys.argv[1:]
    null_non_specz(files)

        
