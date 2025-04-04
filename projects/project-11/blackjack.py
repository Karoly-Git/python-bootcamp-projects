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
    '''Creates a 48-card deck, excluding Jocker'''
    deck = []
    for suit in card_suits.keys():
        for value in card_values:
            deck.append({"name": value["name"], "value": value["value"], "suit": suit})
    
    return deck

def shufle_deck(deck):
    return random.sample(deck, len(deck))

def get_random_card(deck):
    return random.choice(deck)

def remove_card(deck, card):
    return deck.remove(card)

def cards_to_print(cards_list):
    cards_to_print = []
    for card in cards_list:
        cards_to_print.append(card["value"])
    return cards_to_print

def calculate_score(object):
    for card in object["cards"]:
        if card["name"] == "ace":
            if object["score"] + 11 > 21:
                object["score"] += 1
            else:
                object["score"] += 11
        else:
            object["score"] += card["value"]

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
    shufled_deck = shufle_deck(deck)

    while len(player["cards"]) < 2:
        card = get_random_card(shufled_deck)
        player["cards"].append(card)
        remove_card(shufled_deck, card)

    while len(computer["cards"]) < 2:
        card = get_random_card(shufled_deck)
        computer["cards"].append(card)
        remove_card(shufled_deck, card)

    calculate_score(player)
    calculate_score(computer)

    print(f"\tYour cards: {cards_to_print(player["cards"])}, current score: {player["score"]}")
    print(f"\tComputer's first card: {computer["cards"][0]["value"]}")
    
    # Player's loop
    while player["score"] < 21:
        take_another = input("Would you like one more card? Enter 'y' for yes or 'n' for no: ").strip().lower()

        if take_another not in ['y', 'n']:
            print("Invalid input! Enter 'y' for yes or 'n' for no: ")
            continue
        elif take_another == "n":
            print(f"\tYour final hand: {cards_to_print(player["cards"])}, final score: {player["score"]}")
            break
        else:
            card = get_random_card(shufled_deck)
            player["cards"].append(card)
            player["score"] += card["value"]
            remove_card(shufled_deck, card)

            print(f"\tYour cards: {cards_to_print(player["cards"])}, current score: {player["score"]}")

            if player["score"] > 21:
                print("\tIt's a Bust, you lost!")
                return
    
    # Computer's loop
    while computer["score"] < 21:
        card = get_random_card(shufled_deck)
        if computer["score"] + card["value"] > 21:
            print(f"\tComputer's final hand: {cards_to_print(computer["cards"])}, final score: {computer["score"]}")
            break
        computer["cards"].append(card)
        computer["score"] += card["value"]
        remove_card(shufled_deck, card)
            
    # Compare who won
    if player["score"] == computer["score"]:
        print("It's a Draw!")
    elif player["score"] > computer["score"]:
        print("You won!")
    else:
        print("Computer won!")

while True:
    wants_to_play = input("Do you want to play a game of Blackjack? Enter 'y' for yes or 'n' for no: ").strip().lower()

    while wants_to_play not in ['y', 'n']:
        wants_to_play = input("Invalid input! Enter 'y' for yes or 'n' for no: ")
   
    if wants_to_play == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(art.logo)
        play_a_game(card_values, card_suits)
    else:
        print("See you next time!")
        break


#print(cards["7"]["Spades"], cards["Ace"]["Spades"])

