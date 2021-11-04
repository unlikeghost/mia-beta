#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @name: MIA EEG PREPROCESSING MAIN

    @version: 0.1

    @author: Jesus Alan Hernandez Galvan 
"""
import os
import gc
import shutil
from ..libs import constants
from .split import splitData
from .toimg import savearrays
from .merge import mergearray
from .mfccData import mfccExtract
from ..libs.helppers import SaveFile
from .channelsData import channelsExtract

def cehckfolders(path: str):

    if not os.path.exists(path):

        os.mkdir(path)
    
    else:

        shutil.rmtree(path)

        os.mkdir(path)


def preprocessing() -> None:
    """
    Main function

    Returns
    -------
    None

    """

    cehckfolders(constants.TEMPIMAGE)
    cehckfolders(constants.TEMPARRAY)

    print("Channel extract starting...\n")
    data = channelsExtract()

    print("\nMFCC extract starting...\n")
    subjectsMfcc = mfccExtract(data["features"], data["subjects"])

    print("\nSpliting data...\n")
    spliting = splitData(data["features"], constants.TEMPFILE)

    print("\nConverting to img...\n")
    saveimages = savearrays(constants.TEMPFILE, constants.TEMPIMAGE)

    print("\nMerging data...\n")
    merge = mergearray(constants.TEMPIMAGE)

    print("\nSaving data...\n")
    cleanData = SaveFile(constants.CLEANDATAFILE)

    savedata = dict(targets = data["targets"], mfcc = subjectsMfcc)

    cleanData.saveNpz(savedata)

    del cleanData
    gc.collect()

    cleanData = SaveFile(constants.CLEANIMAGESFILE)

    cleanData.saveNpy(merge)

    print(merge.shape)
    del merge
    gc.collect()

    print("\nRemoving temp files\n")
    shutil.rmtree(constants.TEMPIMAGE)
    shutil.rmtree(constants.TEMPARRAY)

    print("\nCleaning memory\n")
    del data 
    del subjectsMfcc
    del spliting
    del saveimages
    del cleanData

    gc.collect()

    print("Done!")


if __name__ == "__main__":

    preprocessing()
    