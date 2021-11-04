#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @name: MIA EEG 

    @version: 0.1

    @author: Jesus Alan Hernandez Galvan 
"""

import sys
import os
import time
import mia

MENU = {"Preprocessing data": mia.preprocessing,
        "Train model": mia.trainmodel,
        "View model": mia.showmodel,
        "Test model": mia.testmodel,
        "Exit Mia": sys.exit}

SUPPORTED_OS = {"linux": "clear",
                "linux2": "clear",
                "win32": "cls"}

METHOD = SUPPORTED_OS.get(sys.platform, lambda: "OS is not supported")


while True:

    for index, option in enumerate(MENU):

        print(f"{index + 1}.- {option}")
    
    selectoption = input("Select option: ")


    try:

        selectoption = int(selectoption)

            
        if selectoption > len(MENU) or selectoption <= 0:

            print("Invalid option!")
        
        else:
            
            key = list(MENU.keys())[selectoption - 1]

            os.system(METHOD)

            MENU[key]()
    
    except ValueError:

        print("Input must be a number, try again")

        time.sleep(1)

        method = SUPPORTED_OS.get(sys.platform, lambda: "OS is not supported")

        os.system(method)
        