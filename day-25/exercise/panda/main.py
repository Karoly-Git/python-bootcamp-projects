import pandas as pd

# Load weather data
weather_data = pd.read_csv("weather_data.csv")

print("="*50)
print("Weather Data Statistics")
print("="*50)

ave_temp = weather_data["temp"].mean()
min_temp = weather_data["temp"].min()
max_temp = weather_data["temp"].max()
round_temp = round(ave_temp, 1)

print(f"Minimum Temperature: {min_temp}°C")
print(f"Maximum Temperature: {max_temp}°C")
print(f"Average Temperature: {round_temp}°C")


print("\n" + "="*50)
print("Student Scores DataFrame")
print("="*50)

# Create the dictionary
student_scores = {
    "student": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
}

# Create DataFrame from dictionary
student_data = pd.DataFrame(student_scores)

# Display DataFrame
print(student_data.to_string(index=False))

# Save data to CSV file
student_data.to_csv("student_scores.csv", index=False)

print("\nData successfully saved to student_scores.csv")