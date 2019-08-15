#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:37:49 2019

Rock, Paper, Scissors app: Implements the classic zero-sum game often
used to make a decision when two parties disagree on the options. This
version pits a user against the computer. The user makes a random choice
between the three options and the computer in turn makes a random selection.
This is repeated three times and whoever wins two of the rounds is the
overall winner.

@author: sansuikyo
"""

import random

choices = ["rock", "paper", "scissors"]

# Player 0 is the user, player 1 is the computer. An outcome matrix is 
# constructed below, with -1 indicating a draw, 0 means player 0 wins,
# and 1 means player 1 wins. The indicies are based on the choices list
# above, with index 0 = "rock", index 1 = "paper", and index 2 = "scissors".
#
outcomes = [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]

game_round = 1
user_wins = 0
computer_wins = 0

while game_round <= 3:
    user_choice = input("\nRock, paper, or scissors? ")
    user_choice = user_choice.strip().lower()
    try:
        user_choice_index = choices.index(user_choice)
    except:
        print("Invalid choice!")
        continue

    # Randomly choose an option for the computer
    computer_choice = random.choice(choices)
    print("Computer's choice: " + computer_choice)
    computer_choice_index = choices.index(computer_choice)
    outcome = outcomes[computer_choice_index][user_choice_index]

    # Determine the outcome for the round. Again, -1 is a draw, 0 is
    # a win for the user, and 1 is a win for the computer    
    if outcome == -1:
        print("It's a draw!")
    elif outcome == 0:
        print("You win round " + str(game_round) + "!")
        user_wins += 1
    else:
        print("The computer wins round " + str(game_round) + "!")
        computer_wins += 1
    
    game_round += 1

# Game is over, determine the winner.
print('\n')
if user_wins > 1:
    print("You win the game!")
elif computer_wins > 1:
    print("The computer wins the game!")
else:
    print("No winner, the game is a draw!")