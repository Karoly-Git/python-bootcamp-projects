MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0  # Global variable to track machine's earnings


def switch_off():
    print("Machine is switching OFF")


def print_report():
    print("Resources:")
    print(f"\tWater:  {resources['water']}ml")
    print(f"\tMilk:   {resources['milk']}ml")
    print(f"\tCoffee: {resources['coffee']}g")
    print(f"\tMoney:  ${money:.2f}")


def check_resources(drink):
    missing = [
        ing for ing, amt in MENU[drink]["ingredients"].items()
        if resources.get(ing, 0) < amt
    ]

    if missing:
        print(f"Sorry, not enough {', '.join(missing)} to make {drink}.")
        return False
    return True


def process_coins():
    coin_values = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }
    total = 0.0

    for coin, value in coin_values.items():
        try:
            count = int(input(f"How many {coin}?: "))
            total += count * value
        except ValueError:
            print(f"Invalid input for {coin}. Counting as 0.")

    return total


def check_transaction_success(paid, price):
    return paid >= price


def make_drink(drink):
    global money
    for ing, amt in MENU[drink]["ingredients"].items():
        resources[ing] -= amt
    money += MENU[drink]["cost"]
    print(f"Enjoy your {drink}!")


def run_coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        while choice not in ["off", "report", "espresso", "latte", "cappuccino"]:
            choice = input("Invalid input! Please enter espresso/latte/cappuccino: ").lower()

        if choice == "off":
            switch_off()
            break
        elif choice == "report":
            print_report()
        else:
            if not check_resources(choice):
                continue

            payment = process_coins()
            cost = MENU[choice]["cost"]

            if check_transaction_success(payment, cost):
                make_drink(choice)
                change = round(payment - cost, 2)
                if change > 0:
                    print(f"Here is your change: ${change}")
            else:
                print("Sorry, that's not enough money. Money refunded.")


run_coffee_machine()
