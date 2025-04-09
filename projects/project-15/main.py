MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def switch_off():
    print("Machine is switching OFF")

def print_report():
    print("Resources:")
    print(f"\tWater:\t{resources['water']}ml")
    print(f"\tMilk:\t{resources['milk']}ml")
    print(f"\tCoffee:\t{resources['coffee']}g")

def check_resources(drink):
    short_ingredients = []

    for ing, amount in MENU[drink]["ingredients"].items():
        if resources.get(ing, 0) < amount:
            short_ingredients.append(ing)

    if short_ingredients:
        print(f"Sorry there is not enough {', '.join(short_ingredients)} to make the selected drink.")
        return False
    return True

def process_coins():
    accepted_coins = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }
    payed = 0.0

    for coin in accepted_coins:
        try:
            coin_count = int(input(f"How many {coin}?: "))
            payed += accepted_coins[coin] * coin_count
        except ValueError:
            payed += 0
    
    return payed

def check_transaction_success(payed, price):
    if payed >= price:
        return True
    return False

def make_drink(drink):
    for ing in MENU[drink]["ingredients"].keys():
        resources[ing] -= MENU[drink]["ingredients"][ing]
    print(f"Enjoy your {drink}!")
        
def run_coffee_machine():
    while True:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

        while drink not in ['off', 'report', 'espresso', 'latte', 'cappuccino']:
            drink = input("Invalid input! Please enter (espresso/latte/cappuccino): ").lower()
        
        if drink == "off":
            switch_off()
            break
        elif drink == "report":
            print_report()
        else:
            if not check_resources(drink):
                continue  # Don't take money if we can't make the drink

            payed = process_coins()
            cost = MENU[drink]["cost"]

            if check_transaction_success(payed, cost):
                make_drink(drink)
                if payed > cost:
                    print(f"Change refunded: ${round(payed - cost, 2)}")
            else:
                print("Sorry that's not enough money. Money refunded.")


run_coffee_machine()
