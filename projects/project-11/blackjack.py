import art
import random

cards = art.cards

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
    # Creates a 48-card deck, excluding Jocker
    deck = []
    for suit in card_suits.keys():
        for value in card_values:
            deck.append({"name": value["name"], "value": value["value"], "suit": suit})
    
    return deck

def shufle_deck(deck):
    return random.sample(deck, len(deck))

deck = make_deck(card_values, card_suits)

shufled_deck = shufle_deck(deck)


for card in shufled_deck:
    print(card)

# over 21: bust
# equal: draw
# lose
# J, Q, K = 1
# A = 1 or 11
# if dealer < 17, has to take one more card

#print(cards["7"]["Spades"], cards["Ace"]["Spades"])
#input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# make the deck
# mix the cards in t deck
# get random card from deck
