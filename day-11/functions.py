import random

# Creates a deck of cards based on the card values and suits.
def make_deck(card_values, card_suits):
    deck = []
    for suit in card_suits.keys():
        for value in card_values:
            deck.append({"name": value["name"], "value": value["value"], "suit": suit})
    
    return deck

# Shuffles the deck randomly.
def shuffle_deck(deck):
    return random.sample(deck, len(deck))

# Returns a random card from the deck.
def get_random_card(deck):
    return random.choice(deck)

# Removes the specified card from the deck.
def remove_card(deck, card):
    return deck.pop(deck.index(card))

# Extracts the value of each card in a list for printing.
def cards_to_print(cards_list):
    cards_to_print = []
    for card in cards_list:
        cards_to_print.append(card["value"])
    return cards_to_print

# Calculates the total score of the player's current cards.
def calculate_score(player_data):
    score = 0
    for card in player_data["cards"]:
        score += card["value"]
    return score

# Adds a card to the player's hand, adjusting the value of an Ace if needed.
def append_card(player_data, card):
    score = calculate_score(player_data)
    if card["name"] == "ace":
        card["value"] = 11 if score + 11 <= 21 else 1
    player_data["cards"].append(card)

# Main function to play a game of Blackjack between the player and computer.
def play_a_game(card_values, card_suits):
    player = {"cards": [], "score": 0}
    computer = {"cards": [], "score": 0}
   
    deck = make_deck(card_values, card_suits)
    shuffled_deck = shuffle_deck(deck)

    # Deal initial cards to player and computer
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
    
    # Player's turn loop
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
                print("It's a Bust, you lost!")
                return
    
    # Computer's turn loop (Computer must hit until it reaches 17 or higher)
    while computer["score"] < 17:
        card = get_random_card(shuffled_deck)
        append_card(computer, card)
        computer["score"] += computer["cards"][-1]["value"]
        remove_card(shuffled_deck, card)
            
    print(f'\tComputer\'s final hand: {cards_to_print(computer["cards"])}, final score: {computer["score"]}')
    
    # Determine the winner
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

#print(cards["7"]["Spades"], cards["Ace"]["Spades"])
