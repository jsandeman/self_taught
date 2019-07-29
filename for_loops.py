#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 12:18:36 2019

@author: jsandeman
"""

### Exercise 1: Print each item in the following list: 
###    ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"].
###
titles = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for t in titles:
    print(t)

### Exercise 2: Print all the numbers from 25 to 50.
###
for i in range(25,51):
    print(i)

### Exercise 3: Print each item in the list from the first challenge and their indexes.
###
i = 0
print("Index\tTitle")
for t in titles:
    print(f"{i}\t{t}")
    i += 1
