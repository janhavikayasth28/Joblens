
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "output" / "cleaned_jobs.csv"

df = pd.read_csv(DATA_FILE)

print("\nCURRENCY COUNTS")
print(df["currency"].value_counts(dropna=False).to_string())

print("\nSALARY SUMMARY BY CURRENCY")
summary = df.groupby("currency", dropna=False).agg(
    job_count=("title", "size"),
    min_salary=("minimumSalary", "min"),
    median_min_salary=("minimumSalary", "median"),
    median_max_salary=("maximumSalary", "median"),
    max_salary=("maximumSalary", "max")
)
print(summary.to_string())

print("\nSAMPLE SALARY RECORDS")
columns = [
    "title", "currency", "salary",
    "minimumSalary", "maximumSalary"
]
print(df[columns].dropna(subset=["minimumSalary", "maximumSalary"])
      .head(15).to_string(index=False))

print("\nZERO SALARY RECORDS")
print(
    ((df["minimumSalary"] == 0) & (df["maximumSalary"] == 0)).sum()
)
