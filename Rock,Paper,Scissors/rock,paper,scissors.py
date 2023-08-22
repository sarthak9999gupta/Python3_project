
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:42:25 2023

@author: sarthakgupta
"""

import random 
comp=random.randint(1,3)
print("Winning rules of the game ROCK PAPER SCISSORS are :\n"
      + "Rock vs Paper -> Rock wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
print("Enter 1 for Rock \n"
      +"Enter 2 For Scissors\n"
      +"Enter 3 For Paper")
user = int(input("enter your choice:"))
if comp==1:
    print("My choice is Rock")
elif comp==3:
    print("My choice is Paper")
elif comp==2:
    print("My choice is Scissors")
while True:
    if comp==user:
        print("Game Draw")
        break
    elif (comp==1 & user==2) or (comp==1 & user==3) or (comp==2 & user==3):
        print("you lose")
        break
    else:
        print("you win")
        break
    
    
