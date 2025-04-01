import art
import os

os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):  # Fixed typo
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return "Error! Division by zero." if n2 == 0 else n1 / n2

operation_map = {
    "+": add, "-": subtract, "*": multiply, "/": divide
}

first_number = None

print(art.logo)

while True:
    while first_number is None:
        try:
            first_number = float(input("What's the first number?: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    operation = input("Pick an operation (+, -, *, /): ")

    while operation not in operation_map:
        operation = input("Invalid operation! Please choose from +, -, *, /: ")

    while True:  # Loop to ensure valid input for next number
        try:
            next_number = float(input("What's the next number?: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    result = operation_map[operation](first_number, next_number)
    
    print(f"{first_number} {operation} {next_number} = {result}")
    
    continue_calc = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").strip().lower()

    if continue_calc == 'y':
        first_number = result if isinstance(result, (int, float)) else None  # Handle division error case
    else:
        first_number = None
        os.system('cls' if os.name == 'nt' else 'clear')
