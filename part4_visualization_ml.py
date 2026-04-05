
# Create students.csv file for download

import pandas as pd

data = [
["Alice",88,92,76,80,95,92,4.5,1],
["Bob",42,55,48,50,60,65,1.2,0],
["Charlie",75,70,80,68,88,85,3.0,1],
["Diana",95,98,91,89,97,98,6.0,1],
["Eve",38,42,50,45,55,58,0.8,0],
["Frank",60,65,72,58,70,78,2.5,1],
["Grace",55,48,44,52,62,60,1.5,0],
["Henry",82,79,85,77,90,88,4.0,1],
["Iris",70,74,68,65,78,80,3.5,1],
["Jack",30,35,40,28,45,50,0.5,0],
["Karen",65,60,70,62,75,72,2.8,1],
["Liam",48,52,44,55,58,62,1.8,0],
["Mia",91,94,88,92,96,95,5.5,1],
["Noah",58,62,55,60,68,70,2.0,0],
["Olivia",78,75,82,70,85,84,3.8,1],
]

columns = ["name","math","science","english","history","pe","attendance_pct","study_hours_per_day","passed"]

df = pd.DataFrame(data, columns=columns)

file_path = "/mnt/data/students.csv"
df.to_csv(file_path, index=False)

file_path

# Load dataset
df = pd.read_csv("students.csv")

# 1. First 5 rows
print("===== First 5 Rows =====")
print(df.head())

# 2. Shape and Data Types
print("\n===== Shape of Dataset =====")
print(df.shape)

print("\n===== Data Types =====")
print(df.dtypes)

# 3. Summary Statistics
print("\n===== Summary Statistics =====")
print(df.describe())

# 4. Pass/Fail Count
print("\n===== Pass/Fail Count =====")
print(df['passed'].value_counts())

# 5. Average Score per Subject (Pass vs Fail)
subject_cols = ['math', 'science', 'english', 'history', 'pe']

pass_avg = df[df['passed'] == 1][subject_cols].mean()
fail_avg = df[df['passed'] == 0][subject_cols].mean()

print("\n===== Average Scores (Pass Students) =====")
print(pass_avg)

print("\n===== Average Scores (Fail Students) =====")
print(fail_avg)

# 6. Student with Highest Average
df['avg_score'] = df[subject_cols].mean(axis=1)

top_student = df.loc[df['avg_score'].idxmax()]

print("\n===== Top Performer =====")
print(f"Name: {top_student['name']}")
print(f"Average Score: {round(top_student['avg_score'], 2)}")