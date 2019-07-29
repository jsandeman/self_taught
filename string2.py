#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:05:49 2019

@author: jsandeman

Second exercise set for string handling in the course The Self-Taught
    Programmer.
"""

### Exercise 1: Find dialogue in your favorite book (containing quotes) and turn it into a string.
###
quote = "Don't tell me about the 'zombies' again. It scares me."
print(quote)

### Exercise 2: Slice the string "It was a bright cold day in April, and the 
###     clocks were striking thirteen." to only include the characters before 
###     the comma
###
sentence = """It was a bright cold day in April, and the clocks 
were striking thirteen."""
first_clause = sentence.split(',')[0]
print(first_clause)

### Exercise 3: Take the list ["The", "fox", "jumped", "over", "the", 
###    "fence", "."] and turn it into a grammatically correct string. There 
###    should be a space between each word, but no space between the word 
###    fence and the period that follows it.
###
words = ["The", "fox", "jumped", "over", "the", "fence", "."]
new_sentence = ' '.join(words[:-1])
final_sentence = new_sentence + words[-1]
print(final_sentence)
