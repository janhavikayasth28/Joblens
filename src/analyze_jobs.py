
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load dataset
files = list(DATA_DIR.glob("*.xlsx"))

if not files:
    raise FileNotFoundError("No Excel dataset found inside data/")

df = pd.read_excel(files[0])

print("Original rows:", len(df))

# Standardize column names
df.columns = df.columns.str.strip()

# Remove exact duplicate rows
before = len(df)
df = df.drop_duplicates()
print("Duplicate rows removed:", before - len(df))

# Clean text fields
text_columns = [
    "title", "companyName", "tagsAndSkills",
    "experience", "location", "jobDescription"
]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()

# Treat blank text as missing
for col in text_columns:
    df[col] = df[col].replace("", pd.NA)

# Convert numeric columns safely
numeric_columns = [
    "minimumSalary", "maximumSalary",
    "minimumExperience", "maximumExperience",
    "ReviewsCount", "AggregateRating"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows without a job title
df = df.dropna(subset=["title"])

# Save cleaned data
df.to_csv(OUTPUT_DIR / "cleaned_jobs.csv", index=False)

# Report 1: Most common job titles
df["title"].value_counts().head(20).rename_axis(
    "job_title"
).reset_index(name="job_count").to_csv(
    OUTPUT_DIR / "top_job_titles.csv", index=False
)

# Report 2: Most common locations
df["location"].value_counts().head(20).rename_axis(
    "location"
).reset_index(name="job_count").to_csv(
    OUTPUT_DIR / "top_locations.csv", index=False
)

# Report 3: Salary range by job title
salary_data = df.dropna(
    subset=["minimumSalary", "maximumSalary"]
).copy()

salary_data = salary_data[
    (salary_data["minimumSalary"] > 0)
    & (salary_data["maximumSalary"] >= salary_data["minimumSalary"])
]

salary_data.groupby("title").agg(
    job_count=("title", "size"),
    avg_min_salary=("minimumSalary", "mean"),
    avg_max_salary=("maximumSalary", "mean")
).sort_values(
    "job_count", ascending=False
).head(100).round(2).to_csv(
    OUTPUT_DIR / "salary_analysis.csv"
)

# Report 4: Missing values after cleaning
df.isna().sum().rename(
    "missing_count"
).to_csv(OUTPUT_DIR / "missing_values_report.csv")

print("\nCLEANING COMPLETE!")
print("Final rows:", len(df))
print("Final columns:", len(df.columns))
print("Reports saved in:", OUTPUT_DIR)
print("\nGenerated files:")
for file in sorted(OUTPUT_DIR.iterdir()):
    print("-", file.name)

