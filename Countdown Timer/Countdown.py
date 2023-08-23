#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 01:13:01 2023

@author: sarthakgupta
"""

import time
def countdown(t):
    while t:
        mins, sec= divmod(t, 60)
        tim='{:02d}:{:02d}'.format(mins,sec)
        time.sleep(1)
        t=t-1
        print(tim,"\n")
        
    print("times up")
    
t=input("Enter Time in secs:")
countdown(int(t))
