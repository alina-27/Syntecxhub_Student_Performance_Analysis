
# Student Performance Analysis Using Python

## Project Overview
This project analyzes student academic performance in Mathematics and Portuguese using Python. It explores grade distributions, study time, absences and correlations with final grades.

## Internship
**Organization:** SYNTECxHUB  
**Project:** Project 2 – Student Performance Analysis  
**Domain:** Data Analytics

## Dataset
Source: [UCI Student Performance Dataset](https://archive.ics.uci.edu/dataset/320/student%2Bperformance)

- Mathematics: 395 records
- Portuguese: 649 records
- Combined: 1,044 course records
- Features: 34 columns

## Tools and Technologies
- Python 3.12
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code
- Git and GitHub

## Project Workflow
1. Dataset download and extraction.
2. Data loading and combination.
3. Data quality inspection.
4. Data preparation and export.
5. Exploratory data analysis.
6. Statistical and correlation analysis.
7. Data visualization.
8. Findings and documentation.

## Key Findings
- Portuguese average final grade: 11.91/20.
- Mathematics average final grade: 10.42/20.
- G1 has a strong positive correlation with G3 (0.809).
- The combined dataset contains no missing values or exact duplicate rows.

## Visualizations
Eight charts are available in the `visualizations/` folder.

## Project Structure

```text
Syntecxhub_Student_Performance_Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── visualizations/
├── reports/
│   └── project_findings.md
│
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

Install dependencies:

```bash
py -3.12 -m pip install -r requirements.txt
```

Run the project:

```bash
py -3.12 main.py
```

## Limitations
- Course records cannot be reliably linked to unique students across subjects.
- Study time is recorded in categories.
- Absences are counts, not attendance percentages.
- Correlation does not imply causation.

## Author
**Feona Fatima**

## Acknowledgement
Dataset provided by the UCI Machine Learning Repository.
