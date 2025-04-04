import art
import functions
import os
import cards

card_values = cards.card_values
card_suits = cards.card_suits
play_a_game = functions.play_a_game

while True:
    wants_to_play = input("Do you want to play a game of Blackjack? Please enter 'y' for yes or 'n' for no: ").strip().lower()

    while wants_to_play not in ["y", "n"]:
        wants_to_play = input("Invalid input! Please enter 'y' for yes or 'n' for no: ")
   
    if wants_to_play == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(art.logo)
        play_a_game(card_values, card_suits)
    else:
        print("See you next time!")
        break
