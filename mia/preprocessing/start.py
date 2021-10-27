#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @name: MIA EEG PREPROCESSING MAIN

    @version: 0.1

    @author: Jesus Alan Hernandez Galvan 
"""

from ..libs import constants
from .mfccData import mfccExtract
from ..libs.helppers import SaveFile
from .channelsData import channelsExtract



def preprocessing() -> None:
    """
    Main function

    Returns
    -------
    None

    """
    
    print("Channel extract starting...")
    data = channelsExtract()

    print("MFCC extract starting...")
    subjectsMfcc = mfccExtract(data["features"], data["subjects"])

    print("Saving data...")
    cleanData = SaveFile(constants.CLEANDATAFILE)

    data["mfcc"] = subjectsMfcc

    cleanData.saveNpz(data)

if __name__ == "__main__":

    preprocessing()