import random
import os
from art import logo
from art import vs
from game_data import data

def choose_random_element(data):
    """
    Selects and returns a random element from the provided data list.

    Parameters:
        data (list): A list of dictionaries, each representing an entity with follower data.

    Returns:
        dict: A randomly selected dictionary from the data list.
    """
    return random.choice(data)

def compare(a, b):
    """
    Compares two entities based on their follower count.

    Parameters:
        a (dict): First entity with a 'follower_count' key.
        b (dict): Second entity with a 'follower_count' key.

    Returns:
        bool: True if entity 'a' has more followers than entity 'b', otherwise False.
    """
    return a['follower_count'] > b['follower_count']

def print_element(element):
    """
    Prints the formatted information of an entity.

    Parameters:
        element (dict): The entity to display, containing 'name', 'description', and 'country'.
    """
    print(f"Compare A: {element['name']}, a {element['description']}, from {element['country']}")

def game(data):
    """
    Runs a round of the Higher Lower game.

    Parameters:
        data (list): A list of dictionaries containing entities with follower count data.

    Behavior:
        - Randomly selects two different entities to compare.
        - Prompts the user to guess which has more followers.
        - Continues until the user makes an incorrect guess.
        - Displays and updates score throughout the session.
    """
    score = 0
    elem_a = choose_random_element(data)
    elem_b = choose_random_element(data)

    while elem_a['name'] == elem_b['name']:
        elem_b = choose_random_element(data)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)

        if score != 0:
            print(f"You're right! Current score: {score}")

        print_element(elem_a)
        print(vs)
        print_element(elem_b)

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
        while answer not in ['a', 'b']:
            answer = input("Wrong input! Type 'A' or 'B': ").lower()

        if (answer == 'a' and compare(elem_a, elem_b)) or (answer == 'b' and not compare(elem_a, elem_b)):
            score += 1
            elem_a = elem_b
            elem_b = choose_random_element(data)
            while elem_a['name'] == elem_b['name']:
                elem_b = choose_random_element(data)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f"Sorry, that's wrong! Final score: {score}")
            break

def main():
    """
    The main loop for the Higher Lower game.

    Behavior:
        - Runs the game.
        - Prompts the user to play again after each round.
        - Exits if the user chooses not to replay.
    """
    while True:
        game(data)
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

main()
