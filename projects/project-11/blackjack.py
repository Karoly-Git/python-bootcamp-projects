import art
import random
import os

card_values = [
    {"name": "ace", "value": 1},
    {"name": "2", "value": 2},
    {"name": "3", "value": 3},
    {"name": "4", "value": 4},
    {"name": "5", "value": 5},
    {"name": "6", "value": 6},
    {"name": "7", "value": 7},
    {"name": "8", "value": 8},
    {"name": "9", "value": 9},
    {"name": "10", "value": 10},
    {"name": "jack", "value": 10},
    {"name": "queen", "value": 10},
    {"name": "king", "value": 10}
]

card_suits = {
    "hearts": "♥",
    "diamonds": "♦",
    "clubs": "♣",
    "spades": "♠"
}

def make_deck(card_values, card_suits):
    '''Creates a 52-card deck, excluding Jocker'''
    deck = []
    for suit in card_suits.keys():
        for value in card_values:
            deck.append({"name": value["name"], "value": value["value"], "suit": suit})
    
    return deck

def shuffle_deck(deck):
    return random.sample(deck, len(deck))

def get_random_card(deck):
    return random.choice(deck)

def remove_card(deck, card):
    return deck.pop(deck.index(card))

def cards_to_print(cards_list):
    cards_to_print = []
    for card in cards_list:
        cards_to_print.append(card["value"])
    return cards_to_print

def calculate_score(player_data):
    score = 0
    for card in player_data["cards"]:
        score += card["value"]
    return score

def append_card(player_data, card):
    score = calculate_score(player_data)
    if card["name"] == "ace":
        card["value"] = 11 if score + 11 <= 21 else 1
    player_data["cards"].append(card)

def play_a_game(card_values, card_suits):
    player = {
        "cards": [],
        "score": 0
    }

    computer = {
        "cards": [],
        "score": 0
    }
   
    deck = make_deck(card_values, card_suits)
    shuffled_deck = shuffle_deck(deck)

    while len(player["cards"]) < 2:
        card = get_random_card(shuffled_deck)
        append_card(player, card)
        player["score"] = calculate_score(player)
        remove_card(shuffled_deck, card)

    while len(computer["cards"]) < 2:
        card = get_random_card(shuffled_deck)
        append_card(computer, card)
        computer["score"] = calculate_score(computer)
        remove_card(shuffled_deck, card)

    print(f'\tYour cards: {cards_to_print(player["cards"])}, current score: {player["score"]}')
    print(f'\tComputer\'s first card: {computer["cards"][0]["value"]}')
    
    # Player's loop
    while player["score"] < 21:
        take_another = input("Would you like one more card? Please enter 'y' for yes or 'n' for no: ").strip().lower()

        if take_another not in ["y", "n"]:
            print("Invalid input! Please enter 'y' for yes or 'n' for no: ")
            continue
        elif take_another == "n":
            print(f'\tYour final hand: {cards_to_print(player["cards"])}, final score: {player["score"]}')
            break
        else:
            card = get_random_card(shuffled_deck)
            append_card(player, card)
            player["score"] += player["cards"][-1]["value"]
            remove_card(shuffled_deck, card)

            print(f'\tYour cards: {cards_to_print(player["cards"])}, current score: {player["score"]}')

            if player["score"] > 21:
                print("\tIt's a Bust, you lost!")
                return
    
    # Computer's loop
    while computer["score"] < 17:
        card = get_random_card(shuffled_deck)
        append_card(computer, card)
        computer["score"] += computer["cards"][-1]["value"]
        remove_card(shuffled_deck, card)
            
    print(f'\tComputer\'s final hand: {cards_to_print(computer["cards"])}, final score: {computer["score"]}')
    
    # Get the winner
    if player["score"] > 21:
        print("It's a Bust, you lost!")
    elif computer["score"] > 21:
        print("Computer busted! You win! 🎉")
    elif player["score"] == computer["score"]:
        print("A draw! You were this close... 🤏")
    elif player["score"] > computer["score"]:
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")

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


#print(cards["7"]["Spades"], cards["Ace"]["Spades"])

