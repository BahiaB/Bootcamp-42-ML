import random
import sys

num = random.randint(0,3)
print(f'This is an interactive guessing game!')
print(f'You have to enter a number between 1 and 99 to find out the secret number.')
print(f'Type exit() to end the game.')   
print(f'Good luck')

attempt = 0
while attempt < 5:
    guess = input("what's your guess between 1 and 99?\n")
    try:
        guess = int(guess)
    except ValueError:
        print("this is not a number")
    if guess > num:
        print("too high")
    elif guess < num:
        print("too low")
    else:
        print("Congratulations, you've got it! \n")
        break
    attempt += 1
print("Dommage")


