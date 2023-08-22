#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:55:33 2023

@author: sarthakgupta
"""

import random
user=int(input("Enter a Number in Range 0-10:"))
comp=random.randint(1, 10)
attempt = 1 
while user!=comp:
        if user==comp:
            attempt=attempt+1
            print("****YOU WON IN ",attempt,"ATTEMPTS****")
            break
        elif user>10 or user<0:
            print("**********Guessed number is out of Range**********")
            user=int(input("Enter number again:"))
            attempt=attempt+1
            continue
        elif user>comp:
            print("Guessed number is too high")
            user=int(input("Enter number again:"))
            attempt=attempt+1
            continue
        elif user<comp:
            print("Guessed number is too low")
            user=int(input("Enter number again:"))
            attempt=attempt+1
            continue
if user==comp:
    print("****YOU WON IN ",attempt,"ATTEMPTS****")
