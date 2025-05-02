import csv

# 1. Working with simple file reading
print("\n" + "="*40)
print("Simple File Reading:")
print("="*40)

with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    for row in data:
        print(row.strip())  # .strip() removes extra newlines


# 2. Working with CSV module
print("\n" + "="*40)
print("CSV Module Reading:")
print("="*40)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(", ".join(row))  # Joins CSV elements clearly
