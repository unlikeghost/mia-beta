import os
import gc
import glob
import numpy as np
from tqdm import tqdm

def mergearray(tempfolder: str, ) -> np.array:

    arrays = []

    for filex in tqdm(glob.glob(os.path.join(tempfolder, "*"))):

        current = np.load(filex, mmap_mode = "r")

        arrays.extend(current)

        del current
        gc.collect()

    return np.array(arrays)

if __name__ == "__main__":
    pass
