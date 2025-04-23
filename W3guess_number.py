#Specification 
#The task is to create a guessing game where the user has to guess the hidden number in as few 
#guesses as possible. 
#After each guess the program responds in one of 3 ways: 
#• The secret number is lower than your guess. Guess again. 
#• The secret number is higher than your guess. Guess again. 
#• You have guessed the secret number! Well done. Game over. 
#You should design an appropriate iterative structure for the game so that it can be played to 
#completion. 
#You should store the sequence of guesses in an appropriate data structure so that you can show the 
#user their game play when the game is over. 

#Extension 
#You should limit the user to a maximum number of guesses, to ensure completion. 
#If the user exceeds this limit you should respond: 
#• You could not guess the secret number in X tries. Unlucky! The number was Y 
#Think about a sensible limit for the number of guesses. 
#Can you design a sensible strategy for this game? 
#Can you estimate the upper bound on the number of tries using that strategy? 
#You can test this by using your program. 

import random

secret_number = random.randint(1, 100)
user_guess_list = []

tries = 0
max_tries = 5

user_guess = int(input("Enter your guess (between 1 and 100): "))

while user_guess != secret_number and tries < max_tries:
    user_guess_list.append(user_guess)
    tries += 1

    # Hint if close
    if abs(user_guess - secret_number) <= 5:
        print("You're very close!")

    # Usual feedback
    if user_guess > secret_number:
        print("The secret number is lower than your guess.")
    else:
        print("The secret number is higher than your guess.")

    # Only ask again if they still have tries left
    if tries < max_tries:
        user_guess = int(input("Try again: "))

# Final result
if user_guess == secret_number:
    user_guess_list.append(user_guess)
    print("You have guessed the secret number! Well done.")
else:
    print("Game over. You've used all your tries!")
    print(f"The secret number was: {secret_number}")

print("Your guesses were:", user_guess_list)
