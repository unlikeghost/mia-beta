#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from typing import List

DERIVATESFILE = os.path.join("mia", "static", "raw_data", "derivatives")

EXCLUDEDCHANNELSFILE = os.path.join("mia", "static", "channels", "ExcludeChannelsEEG.txt")

CLEANDATAFILE = os.path.join("mia", "static", "data", "data.npz")

__all__ = List[str]