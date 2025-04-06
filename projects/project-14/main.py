import random
import os
from art import logo
from art import vs
from game_data import data

def choose_random_element(data):
    return random.choice(data)

def compare(a, b):
    return a['follower_count'] > b['follower_count']

def print_element(element):
    print(f"Compare A: {element['name']}, a {element['description']}, from {element['country']}")


def game(data):
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
    while True:
        game(data)
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


main()