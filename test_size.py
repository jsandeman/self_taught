#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 05:06:11 2019

@author: jsandeman
"""

x: int = 0
while True:
    x = input("Enter a number: ")
    try:
        n = int(x)
        if (n > 10):
            print(f"{n} is greater than 10")
        else:
            print(f"{n} is less than or equal to 10")
    except:
        break
    
7