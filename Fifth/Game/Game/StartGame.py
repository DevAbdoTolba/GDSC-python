from Game.EditValues import *
import random

def main():
    """
    Main function to run the game.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("What's your guess? "))
        attempts += 1
        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
        elif guess < number:
            print("Too low! Guess again.")
        else:
            print("Too high! Guess again.")


if __name__ == '__main__':
    main()
