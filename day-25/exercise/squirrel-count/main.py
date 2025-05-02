import pandas as pd

# Read the data
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get unique fur colors, excluding NaN
colors = data["Primary Fur Color"].dropna().unique().tolist()

print("Unique Fur Colors:", colors)

# Count squirrels by fur color
squirrel_count = {
    "Fur Color": [],
    "Count": []
}

for color in colors:
    count = len(data[data["Primary Fur Color"] == color])
    squirrel_count["Fur Color"].append(color)
    squirrel_count["Count"].append(count)

# Create a DataFrame from the dictionary
squirrel_df = pd.DataFrame(squirrel_count)

# Show the result
print("\nSquirrel Color Count:")
print(squirrel_df)

# Optionally, save it
squirrel_df.to_csv("squirrel_color_count.csv", index=False)
