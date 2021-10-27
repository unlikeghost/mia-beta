#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    @name: MIA EEG 

    @version: 0.1

    @author: Jesus Alan Hernandez Galvan 
"""


import sys

from .preprocessing import startpreprocessing

def preprocessing():
    """
    
    This function runs preprocessing programs such as:
    
        Channel droping (i'm using 8 channels, all excluded channels are on
                         mia/static/channels/ExcludeChannelsEEG.txt)
    
        Mfcc extraction data (mean of 8 channels mfcc data)

    Returns
    -------
    None.

    """
    
    startpreprocessing()

def trainmodel():
    pass

def showmodel():

    pass

def testmodel():
    pass