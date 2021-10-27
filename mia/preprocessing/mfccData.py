#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @name: MIA EEG PREPROCESSING MFCC

    @version: 0.1

    @author: Jesus Alan Hernandez Galvan 
"""


import numpy as np
from tqdm import tqdm
from librosa.feature import mfcc

SUBJECTSINFO = {"sub-01" : np.array(["F", 56]),
                "sub-02" : np.array(["M", 50]),
                "sub-03" : np.array(["M", 34]),
                "sub-04" : np.array(["F", 24]),
                "sub-05" : np.array(["F", 31]),
                "sub-06" : np.array(["M", 29]),
                "sub-07" : np.array(["M", 26]),
                "sub-08" : np.array(["F", 28]),
                "sub-09" : np.array(["M", 35]),
                "sub-10" : np.array(["M", 31])
                }

SAMPLERATE = 256

def mfccExtract(features: np.array, subjects: np.array) -> np.array:
    """
    

    Parameters
    ----------
    features : np.array
        Eeg features.
    subjects : np.array
        List of subject.

    Returns
    -------
    np.array
        mfcc features and subjects info such as age and sex.

    """

    subjectsMfcc = list()

    infoValues= lambda subject: SUBJECTSINFO[subject]

    infoSubject = list(map(infoValues, subjects))

    for index, feature in tqdm(enumerate(features)):

        for subindex in range(0, 8):

            mfccFeatures = mfcc(feature[subindex], sr = SAMPLERATE, n_fft = 1024)
        
            # mean = np.mean(mfccFeatures, axis = 1)

            # print(mean.shape)
            
            subjectsMfcc.append(mfccFeatures)
        
        means = np.mean(subjectsMfcc, axis = (0, 2))

        infoSubject[index] = np.append(infoSubject[index].T, means.T)
    
        subjectsMfcc.clear()     

    return np.array(infoSubject)

if __name__ == "__main__":

    pass
