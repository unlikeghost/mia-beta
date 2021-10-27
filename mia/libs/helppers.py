#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from mne import read_epochs

class ReadFile:

    def __init__(self, file) -> None:
        
        self.file = file
    
    def readFif(self) -> object:

        return read_epochs(self.file, verbose = False)

    def readDat(self) -> np.array:

        return np.load(self.file, allow_pickle = True)
    
    def readNumpy(self) -> np.object:

        return np.load(self.file)

class SaveFile:

    def __init__(self, filename: str) -> None:

        self.filename = filename
    
    def saveNpy(self, array: np.array) -> None:

        np.save(self.filename, array)
    
    def saveNpz(self, arrays: dict):

        np.savez(self.filename, **arrays)