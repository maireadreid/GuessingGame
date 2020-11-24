# libraryimports set up random number generation
import numpy as np
from random import seed
from random import random

#make computer pick a random number to be the answer
def myRandom():
    '''returns a random integer value between 1 and x'''
    x = 32
    return int( random()*x +1 )

#info for loop set up   
seed(1)
bestCount = 99999 #best count starts at a really high number so there's no way for the user to get it wrong that many times
guessCount = 0 #starts the game - necessary to reset the game
gameCount = 0 #starts the count for the number of games getting the right answer takes

#intro message
print("Welcome to the Guessing Game! The aim of the game is to guess a number between 1 and 32")
print("If you guess the correct answer in more than 4 attempts you get to go again.")
print("If you get it in less than 4 attempts, you win! Good luck :)")
print("")
#loop for guessing game
while (bestCount > 4): 
    correct_ans = myRandom() #gets a random number to guess
    print(correct_ans)
    gameCount = 0 #resets count
    guessCount = 0 #resets count
    while (gameCount == 0):
        userGuess = input("Please guess an integer value from 1 to 32: ")
        userGuess = int(userGuess)
        guessCount = guessCount + 1
        if (userGuess < correct_ans): #if the user guess is lower than the correct ans, tell them
            print("Too Low")
            print("")
            gameCount = 0
        elif (userGuess > correct_ans): #if the user guess is higher than the correct ans, tell them
            print("Too High")
            print("")
            gameCount = 0 
        else: #if the user guess is the same as the correct ans, tell them and end the current game
            print("Correct! You took", guessCount, "attempt(s)")
            print("")
            gameCount = 1 #adds 1 to game count which resets the game for the user to try again
    
    if bestCount > guessCount: #if the best guess is higher than the guess count for the game
        bestCount = guessCount #make the guess count for the game 
        print("Your best score so far is:", bestCount)
        print("")
    else:
        print("Your best score so far is:", bestCount)
        print("")

print("You win!")
