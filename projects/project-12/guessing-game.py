import os
from random import randint
from art import logo

# Print logo and starting messages
def intro():
    print(logo)
    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100... Can you guess what it is?")

# Generate a random number between 1 and 100 as the goal
def set_goal_number():
    return randint(1, 100)

# Ask user to choose difficulty and validate input
def set_difficulty():
    difficulty = input("Choose your difficulty — type 'e' for easy or 'h' for hard: ").lower()

    while difficulty not in ["e", "h"]:
        difficulty = input("Oops! Please enter 'e' for easy or 'h' for hard: ").lower()
    
    return difficulty

# Return the number of attempts based on difficulty
def set_attempts(difficulty):
    return 10 if difficulty == 'e' else 5

# Handle the main guessing loop, checking user's guess and giving feedback
def check_answer(attempts, goal_number):
    while attempts > 0:
        print(f"\n🔢 You have {attempts} attempt{'s' if attempts > 1 else ''} left.")
        try:
            guess = int(input("👉 Enter your guess: "))

            if guess == goal_number:
                print(f"\n🎯 Nailed it! The number was {goal_number}. Well done!")
                return
            elif guess < goal_number:
                print("📉 Too low.")
            else:
                print("📈 Too high.")

            attempts -= 1

        except ValueError:
            print("⚠️  Invalid input! Please enter a whole number.")

    print(f"\n💥 You're out of attempts! The number was {goal_number}. Better luck next time!")

# Start a new game round
def play_a_game():
    intro()
    attempts = set_attempts(set_difficulty())
    goal_number = set_goal_number()
    check_answer(attempts, goal_number)

# Ask if the user wants to replay the game
def ask_replay():
    again = input("\n🔁 Would you like to play again? (y/n): ").lower()
    return again == 'y'

# Game loop — clears screen and runs game until user quits
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    play_a_game()
    if not ask_replay():
        print("\n👋 Thanks for playing! See you next time!")
        break
