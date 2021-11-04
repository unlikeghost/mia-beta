import gc
import numpy as np
from tqdm import tqdm

def splitData(features: np.array, savefile: str) -> np.array:
    """
    

    Parameters
    ----------
    features : np.array
        Eeg features.

    Returns
    -------
    np.array

        save splited array features

    """

    samples = np.arange(0, len(features) + 1 , 12)

    arrays = dict()

    for index,_ in tqdm(enumerate(samples)):

        if index + 1 < len(samples):

            arrays[f"{index}"] = features[samples[index]: samples[index + 1]]

    np.savez(savefile, **arrays)

    del arrays
    del samples
    gc.collect()

if __name__ == "__main__":
    pass
