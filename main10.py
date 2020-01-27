#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') # Pring "Greetings" when game begin. 
colors = ['red','orange','yellow','green','blue','violet','purple'] # create a range of the color that pyhton to choose become a right answer
play_again = ''
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): # Use while code to create a loop make game can play again and again, and create the code that player can say no to quit the game
    match_color = random.choice(colors) # allow python to randomly choose one color from the list that is create at line 8
    count = 0
    color = ''
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() # To make the answer keep lowercase and no spaces before or after word
        count += 1 # To count the number of guessing until player answer correct 
        if (color == match_color): # use if code to seperate correct and incorrect answer
            print('Correct!') # when the player got correct answer of random color that python chooses in line 8, it will print "correct!" 
        else: # if player got incorrect answer, it will have different result.
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # if player choose wrong answer, python will tell player how many guess that player try, and tell player try again.
    
    print('\nYou guessed it in {} tries!'.format(count)) # when player win it will tell player total guess that player try until they got final answer.

    if (count < best_count): # if player guesses the right answer less than they did before
        print('This was your best guess so far!') # it will show this string when you got least number of guessing
        best_count = count # the best count will equal to count when count < best_count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() # ask player would like to play again or no, use yes or no to answer, and keep the lowercase and no spaces before and after word.

print('Thanks for playing!') # when game is over, show the string.