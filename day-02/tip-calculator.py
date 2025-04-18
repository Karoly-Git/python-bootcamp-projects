print("Welcome to the London Tip Calculator!")

# Get user inputs
total = float(input("Enter the total bill amount (£): "))

tip_percent = float(input("Enter the tip percentage (e.g., 10, 12, 15): "))

num_of_people = int(input("Enter the number of people splitting the bill: "))

# Calculate cost per person
cost_per_person = total * (1 + tip_percent / 100) / num_of_people

# Format the result to two decimal places
print(f"Each person should pay: £{round(cost_per_person, 2)}")
