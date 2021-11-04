#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from typing import List

DERIVATESFILE = os.path.join("mia", "static", "raw_data", "derivatives")

EXCLUDEDCHANNELSFILE = os.path.join("mia", "static", "channels", "ExcludeChannelsEEG.txt")

CLEANDATAFILE = os.path.join("mia", "static", "data", "data.npz")

CLEANIMAGESFILE = os.path.join("mia", "static", "data", "images.npy")

TEMPFILE = os.path.join("mia", "static", "temp", "arrays", "temp.npz")

TEMPIMAGE = os.path.join("mia", "static", "temp", "images")

TEMPARRAY = os.path.join("mia", "static", "temp", "arrays")

__all__ = List[str]
