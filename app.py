import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
<style>
    .main {
        background-color: #f7f8fc;
    }
    h1 {
        color: #172554;
    }
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/student_performance_cleaned.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error("Dataset not found. Please check the processed data folder.")
    st.stop()

# ---------------- HEADER ----------------
st.title("🎓 Student Performance Analytics")
st.write(
    "An interactive dashboard exploring student academic performance "
    "in Mathematics and Portuguese."
)

st.divider()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Dashboard Filters")

subjects = ["All"] + sorted(df["Subject"].dropna().unique().tolist())

selected_subject = st.sidebar.selectbox(
    "Select Subject",
    subjects
)

filtered_df = df.copy()

if selected_subject != "All":
    filtered_df = filtered_df[
        filtered_df["Subject"] == selected_subject
    ]

# ---------------- KEY METRICS ----------------
st.subheader("Performance Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Course Records",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Average Final Grade",
    f"{filtered_df['G3'].mean():.2f}/20"
)

col3.metric(
    "Average First Period",
    f"{filtered_df['G1'].mean():.2f}/20"
)

col4.metric(
    "Average Second Period",
    f"{filtered_df['G2'].mean():.2f}/20"
)

st.divider()

# ---------------- SUBJECT PERFORMANCE ----------------
st.subheader("📊 Subject Performance")

subject_average = (
    filtered_df.groupby("Subject")[["G1", "G2", "G3"]]
    .mean()
    .round(2)
)

col1, col2 = st.columns(2)

with col1:
    st.write("**Average Grades by Subject**")
    st.bar_chart(subject_average)

with col2:
    st.write("**Grade Statistics**")
    st.dataframe(
        filtered_df[["G1", "G2", "G3"]].describe().round(2),
        use_container_width=True
    )

st.divider()

# ---------------- GRADE DISTRIBUTION ----------------
st.subheader("📈 Final Grade Distribution")

grade_distribution = (
    filtered_df["G3"]
    .value_counts()
    .sort_index()
)

st.bar_chart(grade_distribution)

st.caption("Distribution of final grades (G3), measured on a scale of 0–20.")

st.divider()

# ---------------- STUDY TIME ANALYSIS ----------------
if "studytime" in filtered_df.columns:
    st.subheader("📚 Study Time and Academic Performance")

    study_analysis = (
        filtered_df.groupby("studytime")["G3"]
        .mean()
        .round(2)
    )

    st.bar_chart(study_analysis)

    st.caption(
        "Study time is recorded in categories, from less than 2 hours "
        "to more than 10 hours per week."
    )

st.divider()

# ---------------- ABSENCES ANALYSIS ----------------
if "absences" in filtered_df.columns:
    st.subheader("📉 Absences and Final Grades")

    st.scatter_chart(
        filtered_df,
        x="absences",
        y="G3",
        color="Subject"
    )

    st.caption(
        "This chart explores the relationship between recorded absences "
        "and final grades. It does not establish causation."
    )

st.divider()

# ---------------- CORRELATION ANALYSIS ----------------
st.subheader("🔍 Factors Associated with Final Grades")

numeric_df = filtered_df.select_dtypes(include="number")

if "G3" in numeric_df.columns:
    correlations = (
        numeric_df.corr()["G3"]
        .drop("G3")
        .sort_values(ascending=False)
        .to_frame(name="Correlation with G3")
    )

    st.dataframe(
        correlations.round(3),
        use_container_width=True
    )

    st.caption(
        "Correlation indicates association, not proof that one factor causes another."
    )

st.divider()

# ---------------- RAW DATA ----------------
st.subheader("📋 Explore Student Records")

st.write("View the records included in the selected dashboard filter.")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=350
)

# ---------------- FOOTER ----------------
st.divider()

st.markdown(
    "<center>Student Performance Analysis Project | "
    "Built with Python, Pandas and Streamlit</center>",
    unsafe_allow_html=True
)