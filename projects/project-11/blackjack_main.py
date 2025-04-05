import os
from functions import play_a_game
from cards import card_values
from cards import card_suits
from art import logo

while True:
    wants_to_play = input("Would you like to play a fun game of Blackjack? (y/n): ").strip().lower()

    while wants_to_play not in ["y", "n"]:
        wants_to_play = input("Oops! Please enter 'y' for yes or 'n' for no: ").strip().lower()
   
    if wants_to_play == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        play_a_game(card_values, card_suits)
    else:
        print("Thanks for stopping by! See you next time!")
        break
