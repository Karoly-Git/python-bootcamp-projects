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

wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


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
        player["cards"].append(card)
        remove_card(shufled_deck, card)

    for card in player["card"]:
        player["score"] += card["value"] # if Ace?

    for card in computer["card"]:
        computer["score"] += card["value"] # if Ace?
      


    # print(f"Your cards: [{players_card_1["value"]} {players_card_2["value"]}], current score: {player_score}")

    # print(f"Computer's first card: {computer_card_1["value"]}")

    # user_want = input("Type 'y' to get another card, type 'n' to pass: ")

    return 

if wants_to_play in ["y", "Y"]:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    play_a_game(card_values, card_suits)
else:
    print("See you next time!")




# over 21: bust
# equal: draw
# lose
# J, Q, K = 1
# A = 1 or 11
# if dealer < 17, has to take one more card

#print(cards["7"]["Spades"], cards["Ace"]["Spades"])

# make the deck
# mix the cards in t deck
# get random card from deck
