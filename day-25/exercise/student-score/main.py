import pandas as pd

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