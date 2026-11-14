import os
import pandas as pd

# Load Mathematics dataset
math_df = pd.read_csv("data/raw/student-mat.csv", sep=";")

# Load Portuguese dataset
portuguese_df = pd.read_csv("data/raw/student-por.csv", sep=";")

# Add subject column
math_df["Subject"] = "Mathematics"
portuguese_df["Subject"] = "Portuguese"

# Combine both datasets
df = pd.concat([math_df, portuguese_df], ignore_index=True)

# Display dataset information
print("\nMATHEMATICS DATASET:")
print(math_df.shape)

print("\nPORTUGUESE DATASET:")
print(portuguese_df.shape)

print("\nCOMBINED DATASET:")
print(df.shape)

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nCOLUMN NAMES:")
print(df.columns.tolist())


# DATASET QUALITY CHECK

print("\n========== DATASET INFORMATION ==========")
df.info()

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\nTotal missing values:", df.isnull().sum().sum())

print("\n========== DUPLICATE RECORDS ==========")
print("Duplicate rows:", df.duplicated().sum())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# DATA PREPARATION AND EXPORT

# Create a separate copy for analysis
cleaned_df = df.copy()

# Check grade values
print("\n========== GRADE VALIDATION ==========")
print("Minimum G3:", cleaned_df["G3"].min())
print("Maximum G3:", cleaned_df["G3"].max())

# Save prepared dataset
os.makedirs("data/processed", exist_ok=True)

cleaned_df.to_csv(
    "data/processed/student_performance_cleaned.csv",
    index=False
)

# Create subject-wise summary
subject_summary = cleaned_df.groupby("Subject")[["G1", "G2", "G3"]].mean()

subject_summary.to_csv(
    "data/processed/subject_summary.csv"
)

print("\nPrepared dataset saved successfully!")
print("Subject summary saved successfully!")
print("\nSUBJECT-WISE GRADE AVERAGES:")
print(subject_summary)

# ==========================================
# DATA VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

# Create visualizations folder
os.makedirs("visualizations", exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Average final grade by subject
subject_avg = cleaned_df.groupby("Subject")["G3"].mean()

plt.figure(figsize=(8, 5))
plt.bar(subject_avg.index, subject_avg.values)
plt.title("Average Final Grade by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Final Grade (G3)")
plt.ylim(0, 20)
plt.tight_layout()
plt.savefig("visualizations/01_subject_average.png", dpi=300)
plt.close()


# 2. Distribution of final grades
plt.figure(figsize=(8, 5))
sns.histplot(data=cleaned_df, x="G3", bins=21, kde=True)
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("visualizations/02_grade_distribution.png", dpi=300)
plt.close()


# 3. Final grade comparison by subject
plt.figure(figsize=(8, 5))
sns.boxplot(data=cleaned_df, x="Subject", y="G3")
plt.title("Final Grade Comparison by Subject")
plt.xlabel("Subject")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig("visualizations/03_subject_boxplot.png", dpi=300)
plt.close()


# 4. Grade progression (G1, G2, G3)
grade_progression = cleaned_df.groupby("Subject")[
    ["G1", "G2", "G3"]
].mean().T

grade_progression.plot(kind="line", marker="o", figsize=(8, 5))
plt.title("Average Grade Progression by Subject")
plt.xlabel("Assessment Period")
plt.ylabel("Average Grade")
plt.xticks([0, 1, 2], ["G1", "G2", "G3"])
plt.ylim(0, 20)
plt.tight_layout()
plt.savefig("visualizations/04_grade_progression.png", dpi=300)
plt.close()


# 5. Study time vs final grade
plt.figure(figsize=(8, 5))
sns.barplot(data=cleaned_df, x="studytime", y="G3", errorbar=None)
plt.title("Study Time vs Average Final Grade")
plt.xlabel("Study Time Category (1–4)")
plt.ylabel("Average Final Grade")
plt.tight_layout()
plt.savefig("visualizations/05_studytime_vs_grade.png", dpi=300)
plt.close()


# 6. Absences vs final grade
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=cleaned_df,
    x="absences",
    y="G3",
    hue="Subject",
    alpha=0.6
)
plt.title("Absences vs Final Grade")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig("visualizations/06_absences_vs_grade.png", dpi=300)
plt.close()


# 7. Grade category distribution
cleaned_df["Grade_Category"] = pd.cut(
    cleaned_df["G3"],
    bins=[-1, 9, 13, 16, 20],
    labels=["0–9", "10–13", "14–16", "17–20"]
)

plt.figure(figsize=(8, 5))
sns.countplot(
    data=cleaned_df,
    x="Grade_Category",
    order=["0–9", "10–13", "14–16", "17–20"]
)
plt.title("Distribution of Students by Grade Category")
plt.xlabel("Grade Category (Project-defined)")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("visualizations/07_grade_categories.png", dpi=300)
plt.close()


# 8. Correlation heatmap
numeric_df = cleaned_df.select_dtypes(include="number")
correlation = numeric_df.corr()

plt.figure(figsize=(14, 10))
sns.heatmap(correlation, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap of Student Performance")
plt.tight_layout()
plt.savefig("visualizations/08_correlation_heatmap.png", dpi=300)
plt.close()


print("\nAll 8 visualizations created successfully!")
# STATISTICAL ANALYSIS

print("\n========== STATISTICAL ANALYSIS ==========")

# Overall grade statistics
grade_stats = cleaned_df[["G1", "G2", "G3"]].describe()

print("\nGRADE STATISTICS:")
print(grade_stats)

# Subject-wise grade statistics
subject_stats = cleaned_df.groupby("Subject")[["G1", "G2", "G3"]].mean()

print("\nSUBJECT-WISE AVERAGES:")
print(subject_stats)

# Correlation analysis
correlation = cleaned_df.select_dtypes(include="number").corr()

print("\nCORRELATION WITH FINAL GRADE (G3):")
print(correlation["G3"].sort_values(ascending=False))

# Export results
grade_stats.to_csv("data/processed/grade_statistics.csv")
subject_stats.to_csv("data/processed/subject_grade_averages.csv")
correlation.to_csv("data/processed/correlation_matrix.csv")

print("\nStatistical analysis completed and files saved!") 