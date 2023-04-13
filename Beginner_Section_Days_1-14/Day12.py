'''
Day 12 Topic: Scope
Project: Number Guessing Game
'''

# two difficulties: easy(10 guesses) and hard(5 guesses)
#

import random

def checkGuess(guess, goal):

    if guess == goal:
        print("Correct!")
        return 0
    elif guess < goal:
        print("The number is higher.")
        return 1
    else:
        print("The number is lower.")
        return 1

def getGuess(attempts):
    print(f"You have {attempts} remaining to guess the number.")
    return int(input("Make a guess: "))

def game():

    target = random.randrange(1, 101, 1)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 0

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        guess = getGuess(attempts)
        status = checkGuess(guess, target)
        if status == 0:
            attempts = 0
            break
        else:
            attempts -= 1

game()