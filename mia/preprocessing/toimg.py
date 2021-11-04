import os
import gc
import numpy as np
from tqdm import tqdm
from pyts.image import GramianAngularField

TRANSFORMER = GramianAngularField(image_size = 0.15)

def toimg(array: np.array):

    return TRANSFORMER.transform(array)

def savearrays(tempfile: str, savepath: str) -> None:

    arrays = np.load(tempfile, mmap_mode = "r")

    for file in tqdm(arrays._files):

        images = list()

        for feature in arrays[file]:

            image = toimg(feature)

            images.append(image)
        
        np.save(os.path.join(savepath, file), np.array(images), allow_pickle = True)

        del images
        gc.collect()

if __name__ == "__main__":
    pass
