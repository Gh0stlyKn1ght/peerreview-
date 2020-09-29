# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Juan Nevarez
# Creation Date: 9/26/2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
    print('You are in a land full of dragons.') # one line print to prevent indent on output
    print('In front of you,you see two caves. In one cave, the dragon is friendly')  #one line print
    print('and will share his treasure with you. The other dragon') #one line print
    print('is greedy and hungry, and will eat you on sight.') #one line print
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave #removed s as it was giving syntax error


def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds #asked for 2 seconds of sleep not 3
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 3 seconds #3 seconds not 2
    time.sleep(3)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print ('Gobbles you down in one bite!')

playAgain = "yes"

while playAgain == 'yes' or playAgain == 'y': #added =, needs 2 ='s to function

    displayIntro()
    caveNumber = chooseCave() #lowercase C in Cave
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == "no":
        print("Thanks for playing") #spelling error in playing fixed

