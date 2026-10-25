
from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "output" / "cleaned_jobs.csv"
OUTPUT_DIR = PROJECT_DIR / "output"
DB_FILE = PROJECT_DIR / "joblens.db"

# Load cleaned job data
df = pd.read_csv(DATA_FILE)

# Create a local SQLite database
with sqlite3.connect(DB_FILE) as conn:
    df.to_sql("jobs", conn, if_exists="replace", index=False)

    # 1. Top job locations
    top_locations = pd.read_sql_query("""
        SELECT location, COUNT(*) AS job_count
        FROM jobs
        WHERE location IS NOT NULL AND TRIM(location) != ''
        GROUP BY location
        ORDER BY job_count DESC
        LIMIT 10
    """, conn)

    # 2. Most common job titles
    top_titles = pd.read_sql_query("""
        SELECT title, COUNT(*) AS job_count
        FROM jobs
        WHERE title IS NOT NULL AND TRIM(title) != ''
        GROUP BY title
        ORDER BY job_count DESC
        LIMIT 10
    """, conn)

    # 3. Average salary by job title

    # 3. Salary analysis: INR listings with valid positive salary values
    salary_analysis = pd.read_sql_query("""
        SELECT title,
               ROUND(AVG(minimumSalary), 0) AS avg_min_salary_inr,
               ROUND(AVG(maximumSalary), 0) AS avg_max_salary_inr,
               COUNT(*) AS job_count
        FROM jobs
        WHERE currency = 'INR'
          AND minimumSalary > 0
          AND maximumSalary > 0
          AND maximumSalary >= minimumSalary
        GROUP BY title
        HAVING COUNT(*) >= 10
        ORDER BY job_count DESC
        LIMIT 20
    """, conn)


# Save reports
top_locations.to_csv(OUTPUT_DIR / "sql_top_locations.csv", index=False)
top_titles.to_csv(OUTPUT_DIR / "sql_top_titles.csv", index=False)
salary_analysis.to_csv(OUTPUT_DIR / "sql_salary_analysis.csv", index=False)

print("\nTOP 10 JOB LOCATIONS")
print(top_locations.to_string(index=False))

print("\nTOP 10 JOB TITLES")
print(top_titles.to_string(index=False))

print("\nSALARY ANALYSIS")
print(salary_analysis.head(10).to_string(index=False))

print("\nSQL ANALYSIS COMPLETE!")
print("Database saved:", DB_FILE)
print("Reports saved in:", OUTPUT_DIR)
