
# Student Performance Analysis Using Python

## 1. Dataset Overview

The project uses the Student Performance dataset from the UCI Machine Learning Repository. It contains Mathematics and Portuguese student performance records.

- Mathematics records: 395
- Portuguese records: 649
- Combined records: 1,044
- Total columns: 34

## 2. Data Quality Findings

The dataset was checked for missing values, duplicate records and data types.

- Missing values: 0
- Exact duplicate rows: 0
- Final grade range (G3): 0–20
- The two subject datasets were combined into one dataset with a Subject column.

No missing-value treatment was required.

## 3. Overall Grade Statistics

| Statistic | G1 | G2 | G3 |
|---|---:|---:|---:|
| Mean | 11.21 | 11.25 | 11.34 |
| Median | 11 | 11 | 11 |
| Standard Deviation | 2.98 | 3.29 | 3.86 |
| Minimum | 0 | 0 | 0 |
| Maximum | 19 | 19 | 20 |

The overall average grade increases slightly from G1 to G3. The standard deviation also increases, indicating greater variation in final grades.

## 4. Subject-wise Performance

| Subject | G1 | G2 | G3 |
|---|---:|---:|---:|
| Mathematics | 10.91 | 10.71 | 10.42 |
| Portuguese | 11.40 | 11.57 | 11.91 |

Portuguese has a higher average final grade than Mathematics in this combined dataset. Mathematics shows a slight decrease in average grades, while Portuguese shows an increase.

## 5. Correlation Analysis

The correlation analysis identified the following relationships with final grade (G3):

- G1: 0.809 — strong positive correlation.
- Mother's education (Medu): 0.201 — weak positive correlation.
- Study time category: 0.162 — weak positive correlation.
- Father's education (Fedu): 0.160 — weak positive correlation.
- Absences: -0.046 — very weak negative correlation.
- Failures: -0.383 — moderate negative correlation.

G1 has the strongest positive correlation with G3 among the variables examined. Previous academic performance is therefore strongly associated with final performance in this dataset.

Correlation does not establish causation.

## 6. Visualizations Created

The project includes eight visualizations:

1. Average final grade by subject.
2. Distribution of final grades.
3. Final grade comparison by subject.
4. Grade progression across G1, G2 and G3.
5. Study time versus average final grade.
6. Absences versus final grade.
7. Distribution of grade categories.
8. Correlation heatmap.

## 7. Conclusion

The analysis shows differences in Mathematics and Portuguese performance across the three assessments. Portuguese has a higher average final grade in the combined dataset, while G1 has a strong positive correlation with G3.

The project demonstrates how Python libraries such as Pandas, Matplotlib and Seaborn can be used for data preparation, statistical analysis and visualization.

## 8. Limitations

- The dataset does not provide a unique student identifier to link the two subject records reliably.
- The combined 1,044 records represent course records, not necessarily 1,044 unique students.
- Study time is recorded in categories rather than exact hours.
- Absences are recorded as counts, not attendance percentages.
- The analysis identifies associations and does not establish causal relationships.
