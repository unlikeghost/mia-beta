#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @name: MIA EEG PREPROCESSING CHANNELS

    @version: 0.1

    @author: Jesus Alan Hernandez Galvan 
"""

import os
import numpy as np
from tqdm import tqdm 
from ..libs import (helppers,
                    constants)


TARGETSNAME = {0: "Arriba",
               1: "Abajo",
               2: "Derecha",
               3: "Izquierda"}

def dropChannels(Eeg: object, channels: list) -> np.array:
    """
    

    Parameters
    ----------
    Eeg : object
        EEG object itr returned from mne read epochs.
    channels : list
        channels to drop.

    Returns
    -------
    eeg : np.array
        (8,1153) shape channel data.

    """

    eeg = Eeg.drop_channels(channels)
    
    eeg = eeg._data
    
    return eeg

def dropNotinner(target_data: np.array, subject: str) -> list :
    """
    

    Parameters
    ----------
    target_data : np.array
        Array with shape (4, n), where Nicolas Nieto save targets info
        
    subject : str
        Wich subject its currently itering.

    Returns
    -------
    list 
        inner index: index number
        targets:  targets of inner speech
        subject: np.array shabe(1, n)

    """

    innerIndex = np.where(target_data[:,2] == 1)[0]

    only_targets = target_data[innerIndex, 1]

    subject = np.array([subject] * len(only_targets))

    tostr = lambda index: TARGETSNAME[index]
            
    targets = list(map(tostr, only_targets))

    return innerIndex, targets, subject


def channelsExtract() -> dict:
    """
    
    main function that clean all data
    Returns
    -------
    dict
        all cleaned info.

    """

    all_features = list()
    all_targets = list()
    all_subjects = list()

    excluded_channels = open(constants.EXCLUDEDCHANNELSFILE).read().split("-")

    for subject in tqdm(range(1, 11)):

        if subject < 10:

            subject = f"sub-0{subject}"
        
        else:

            subject = f"sub-{subject}"
        
        for session in range(1, 4):

            session = f"ses-0{session}"

            try:

                folder = os.path.join(subject, session)

                features_file = os.path.join(constants.DERIVATESFILE, folder, f"{subject}_{session}_eeg-epo.fif")

                target_file = os.path.join(constants.DERIVATESFILE, folder, f"{subject}_{session}_events.dat")

                target_object = helppers.ReadFile(target_file)

                features_object = helppers.ReadFile(features_file)

                target_data = target_object.readDat()

                feature_data = features_object.readFif()

                eeg = dropChannels(feature_data, excluded_channels)

                innerIndex, targets, subjects = dropNotinner(target_data, subject)

                eeg = eeg[innerIndex, :]
                
                all_features.extend(eeg)
                
                all_targets.extend(targets)
                
                all_subjects.extend(subjects)
            
            except Exception as e:

                print(e)
                print(f"Error {subject} session {session} passed\n")

    return dict(features = np.array(all_features),
                targets = np.array(all_targets),
                subjects = np.array(all_subjects))                 

if __name__ == "__main__":

    channelsExtract()


