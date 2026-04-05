#  Student Performance Analysis and Prediction

##  Overview

I am going to analyze data about students performance. I will use Matplotlib and Seaborn to see trends in the data. Then I will build a Machine Learning model to predict if a student will pass or fail.

The project has 4 parts:

1. I will explore the data using Pandas.

2. I will visualize the data using Matplotlib.

3. I will also visualize the data using Seaborn.

4. I will build a Machine Learning model using Scikit-learn.

##  Dataset

The dataset has information about 15 students. The data includes:

- Grades for subjects like Math, Science, English, History and PE

- How often students attend classes

- How hours students study each day

- Whether the student Passed or Failed (1, for Pass, 0 for Fail)

File used:

---

##  Task 1 — Data Exploration (Pandas)

- Loaded dataset using `pandas`
- Displayed first 5 rows using `.head()`
- Checked dataset shape and data types
- Generated summary statistics using `.describe()`
- Counted pass/fail students using `.value_counts()`
- Computed average subject scores for:
  - Passing students
  - Failing students
- Identified the top-performing student using average score

---

##  Task 2 — Data Visualization (Matplotlib)

Generated and saved the following plots:

1. **Bar Chart** — Average score per subject  
   → `plot1_bar.png`

2. **Histogram** — Distribution of math scores with mean line  
   → `plot2_hist.png`

3. **Scatter Plot** — Study hours vs average score (Pass vs Fail)  
   → `plot3_scatter.png`

4. **Box Plot** — Attendance comparison (Pass vs Fail)  
   → `plot4_box.png`

5. **Line Plot** — Math vs Science scores across students  
   → `plot5_line.png`

---

##  Task 3 — Data Visualization (Seaborn)

Generated advanced visualizations:

1. **Bar Plots (Subplots)** — Average Math & Science scores by Pass/Fail  
   → `plot6_seaborn_bar.png`

2. **Scatter Plot with Regression Lines** — Attendance vs Average Score  
   → `plot7_seaborn_scatter.png`

###  Comparison:
Seaborn simplifies statistical visualization with built-in functions and better styling, whereas Matplotlib requires more manual customization but offers greater flexibility.

---

##  Task 4 — Machine Learning (Scikit-learn)

###  Model Used:
- Logistic Regression

###  Steps:
- Selected features:
  - math, science, english, history, pe, attendance_pct, study_hours_per_day
- Split dataset (80% train, 20% test)
- Applied feature scaling using `StandardScaler`
- Trained model using `LogisticRegression`

###  Evaluation:
- Printed training accuracy
- Printed test accuracy
- Displayed predictions with:
  - Student name
  - Actual result
  - Predicted result
  - Correct/Wrong indicator

###  Feature Importance:
- Extracted model coefficients
- Sorted by importance
- Visualized using bar chart  
  → `plot8_feature_importance.png`

###  Bonus:
- Predicted result for a new student
- Displayed prediction probability

---

##  Project Structure

---

##  How to Run

1. Install required libraries:
 
2. Run the script:

---

##  Conclusion

- Students with higher attendance and study hours tend to perform better.
- Machine learning model successfully predicts pass/fail outcomes.
- Visualization helps in understanding performance trends clearly.

---

##  Author
- Name: Ayushi
