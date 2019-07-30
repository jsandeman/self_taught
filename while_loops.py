#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:09:32 2019

@author: sansuikyo

While loop exercises for The Self-Taught Programmer
"""

### Exercise 1: Write a program with an infinite loop (with the option to type
### q to quit) and a list of numbers. Each time through the loop ask the user
### to guess a number on the list and tell them whether or not they guessed 
### correctly.
num_list = [5, 8, 10, 4, 1]
while True:
    guess = input("Guess a number or 'q' to quit: ")
    if guess.lower() == 'q':
        break
    else:
        try:
            x = int(guess)
            if x in num_list:
                print("Your guess is in the list!")
            else:
                print("Nope, not in the list!")
        except:
            print("Please enter an integer or 'q' to quit.")


### Exercise 2: Multiply all the numbers in the list [8, 19, 148, 4] with all
### the numbers in the list [9, 1, 33, 83], and append each result to a third 
### list.
###
### Since loops are old hat for me, I took the liberty of exploring
### Python's list comprehension to find a compact way of performing this
### task.
###
lista = [8, 19, 148, 4]
listb = [9, 1, 33, 83]
product = [a*b for a,b in zip(lista, listb)]
print(product)
