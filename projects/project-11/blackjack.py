import art

cards = art.cards

card_values = {
    "Hearts":[{"Ace-1": 1},{"2": 2},{"3": 3},{"4": 4},{"5": 5},{"6": 6},{"7": 7},{"8": 8},{"9": 9},{"Jack": 10},{"Queen": 10},{"King": 10}],
    "Diamonds":[{"Ace-1": 1},{"2": 2},{"3": 3},{"4": 4},{"5": 5},{"6": 6},{"7": 7},{"8": 8},{"9": 9},{"Jack": 10},{"Queen": 10},{"King": 10}],
    "Clubs":[{"Ace-1": 1},{"2": 2},{"3": 3},{"4": 4},{"5": 5},{"6": 6},{"7": 7},{"8": 8},{"9": 9},{"Jack": 10},{"Queen": 10},{"King": 10}],
    "Spades":[{"Ace-1": 1},{"2": 2},{"3": 3},{"4": 4},{"5": 5},{"6": 6},{"7": 7},{"8": 8},{"9": 9},{"Jack": 10},{"Queen": 10},{"King": 10}],
}

card_suits = {
    "Hearts": "♥",
    "Diamonds": "♦",
    "Clubs": "♣",
    "Spades": "♠"
}

# over 21: bust
# equal: draw
# lose
# J, Q, K = 1
# A = 1 or 11
# if dealer < 17, has to take one more card

print(cards["7"]["Spades"], cards["Ace"]["Spades"])

input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
