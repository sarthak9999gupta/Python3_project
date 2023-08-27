#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script metadata and author information
"""
Created on Sun Aug 27 14:02:13 2023
@author: sarthakgupta
"""

# Function to compute the sum of three numbers
def sum(a, b, c):
    return a + b + c

# Function to print the Tic-Tac-Toe board state
def board(xstate, zstate):
    # Create the board based on the states of 'X' and 'O' (or '0' in this case)
    # Each variable stores the character to be printed in the corresponding board position
    # Variables are named by board position (zero for position 0, one for position 1, etc.)
    
    # Determine which symbol to place in each cell of the 3x3 grid
    zero, one, two, three, four, five, six, seven, eight = (
        'X' if xstate[i] else ('0' if zstate[i] else str(i)) for i in range(9)
    )
    
    # Print the current board state
    print(f"{zero} | {one} | {two}")
    print("---------")
    print(f"{three} | {four} | {five}")
    print("---------")
    print(f"{six} | {seven} | {eight}")

# Function to check for a win
def checkwin(xstate, zstate):
    # Define all winning combinations
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    # Loop through all winning combinations to check for a win
    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("x wins")
            return 1
        elif sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:
            print("O wins")
            return 0
    return -1  # Return -1 if there's no win

# Initialize board states for 'X' and 'O'
xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Variable to keep track of whose turn it is ('1' for 'X', '0' for 'O')
turn = 1

# Welcome message
print("WELCOME TO TIC_TAC_TOE GAME")

# Main game loop
while True:
    # Display board
    board(xstate, zstate)
    
    # Get the next move
    if turn == 1:
        print("x chance")
        value = int(input("enter a number from board: "))
        xstate[value] = 1
    else:
        print("O chance")
        value = int(input("enter a number in range: "))
        zstate[value] = 1
    
    # Check for a win
    cwin = checkwin(xstate, zstate)
    if cwin != -1:
        print("Match over")
        break  # Exit the loop if the match is over
    
    # Switch turns
    turn = 1 - turn
