#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 05 04:50:15 2019

@author: jsandeman

Hangman app.

This app implements the classic Hangman game, where one player chooses
a word at random and another attempts to guess the word. The guesser may
guess a word at any time, but usually guesses letters to obtain enough clues
to guess the word. If the letter guess is correct, the positions of the letters are
revealed. If the guess is wrong, another segment of a stick figure hanging
from the gallows is drawn. If the drawing is completed before the player
guesses the word, they loose, otherwise, they win.

The course exercise specifies that if a letter occurs more than once in
the word, the player must guess each instance, which is different from
the standard rules above. I decided to implement the standard rules as
it poses some additional challenges for the logic and data srtuctures
required.

The implementation of this app centers around ascertaining the positions
of each letter in the randomly chosen word. A set is created of each
unique letter, and then the word string is scanned. Each index for each
letter is stored in a list in a dictionary where the keys are the letters.
"""
import random, csv


with open("hangman_word_list.csv") as word_file:
    word_data = list(csv.reader(word_file, delimiter=','))
    word_list = [word for row in word_data for word in row]


### The choice() method selects an item from a list at random
word_to_guess = random.choice(word_list)
word_len = len(word_to_guess)

### The current state of the player's guesses are represented by a
### list. Guessed letters are stored in their proper positions and
### unguessed letters are represented by the underscore character.
###
word_guess_state = []
for i in range(0,word_len):
    word_guess_state.append("_")

### This version of hangman does not render a drawing of the gallows.
### Instead, it simply keeps track of an equivalent number of guesses
### assuming the following body parts:
### Head, right eye, left eye, mouth, body, left arm, right arm, left leg,
### right leg (total 9)
###
errors_left = 9

### Create a set of the unique letters in the word to be guessed. Then
### loop through the word and create a dictionary with the letters as 
### keys and a list of the indices where they appear as the values
###
letters = set(word_to_guess)
letter_indices = {}
for c in letters:
    for i, l in enumerate(word_to_guess):
        if c == l:
            if c not in letter_indices:
                letter_indices[c] = [i]
            else:
                letter_indices[c].append(i)


### Now it's time to play! The player may guess either a letter
### or the whole word
###
                
while True:
    guess = input("Guess a letter or the whole word: ")
    guess = guess.lower()
    if len(guess) > 1:
        if guess == word_to_guess:
            print("Congratulations! You won!")
            break
    else:
        if guess not in letters:
            print("This letter in not in the word!")
            errors_left -= 1
            if errors_left < 1:
                print("You're out of guesses! Better luck next time.")
                print("The word was: " + word_to_guess)
                break
            else:
                print("You have " + str(errors_left) + " guesses remaining.")
                print(" ".join(word_guess_state))
        else:
            print("Good guess!")
            indices = letter_indices[guess]
            for i in indices:
                word_guess_state[i] = guess
            print(" ".join(word_guess_state))
            if "_" not in word_guess_state:
                print("Congratulations, you won!")
                break

            