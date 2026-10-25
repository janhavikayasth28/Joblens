
from pathlib import Path
import pandas as pd
from collections import Counter

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "output" / "cleaned_jobs.csv"
OUTPUT_DIR = PROJECT_DIR / "output"

df = pd.read_csv(DATA_FILE)

# Common skills to track
skills_to_find = [
    "python", "sql", "excel", "power bi", "tableau",
    "java", "javascript", "html", "css", "aws",
    "machine learning", "data analysis", "pandas",
    "communication skills", "project management",
    "sap", "salesforce", "powerpoint", "mysql",
    "azure", "accounting", "marketing"
]

skill_counts = Counter()
skill_column = df["tagsAndSkills"].fillna("").str.lower()

for skill in skills_to_find:
    # Match skill names as separate words or phrases
    pattern = r"(?<![a-z0-9])" + skill.replace(" ", r"\s+") + r"(?![a-z0-9])"
    skill_counts[skill] = int(skill_column.str.contains(
        pattern, regex=True, na=False
    ).sum())

result = pd.DataFrame(
    skill_counts.items(),
    columns=["skill", "job_listings"]
)

result = result.sort_values(
    "job_listings", ascending=False
).reset_index(drop=True)

result.to_csv(OUTPUT_DIR / "top_skills_clean.csv", index=False)

print("\nTOP SKILLS IN THE INDIAN JOB MARKET")
print(result.to_string(index=False))
print("\nSaved: output/top_skills_clean.csv")

