# Python number guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {guesses} tries.")
            is_running = False
    else:
        print("Please enter a whole integer number between 1-100.")