import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = input("How many letters would you like in your password?\n")

try:
    nr_letters = int(nr_letters)
except ValueError:
    print("Invalid input.")
    quit()

nr_numbers = input("How many numbers would you like in your password?\n")

try:
    nr_numbers = int(nr_numbers)
except ValueError:
    print("Invalid input.")
    quit()

nr_symbols = input("How many symbols would you like in your password?\n")

try:
    nr_symbols = int(nr_symbols)
except ValueError:
    print("Invalid input.")
    quit()

def chars(list, num_of_chars):
    char_list = []

    for char in range(0, num_of_chars):
        char_list.append(list[random.randint(0, len(list) - 1)])
    
    return char_list
        
password_chars = (
    chars(letters, nr_letters) +
    chars(numbers, nr_numbers) +
    chars(symbols, nr_symbols)
)

random.shuffle(password_chars)

generated_password = "".join(password_chars)

print(generated_password)