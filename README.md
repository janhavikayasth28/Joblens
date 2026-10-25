# JobLens — Indian Job Market & Skills Demand Analyzer

## Project Overview
JobLens is a Python and SQL-based data analytics project that explores job listings in the Indian job market. It analyzes job locations, job titles, skill demand, and available salary information to help identify patterns in the dataset.

## Objectives
- Clean and prepare raw job listing data.
- Identify the most frequently mentioned skills.
- Analyze job listings by location and title using SQL.
- Examine disclosed salary information while excluding zero and USD salary values from the INR salary report.
- Generate CSV reports for further analysis and visualization.

## Technologies Used
- **Python** — data cleaning and analysis
- **Pandas** — data manipulation
- **SQLite** — storing and querying job listing data
- **SQL** — aggregations and analysis
- **Excel / CSV** — input and output data formats
- **Power BI** — planned dashboard development

## Project Structure

```text
JobLens/
├── data/
│   └── indian-job-market-dataset-2025.xlsx
├── output/
│   ├── cleaned_jobs.csv
│   ├── missing_values_report.csv
│   ├── salary_analysis.csv
│   ├── top_job_titles.csv
│   ├── top_locations.csv
│   ├── skill_demand.csv
│   ├── top_skills_clean.csv
│   ├── sql_top_locations.csv
│   ├── sql_top_titles.csv
│   └── sql_salary_analysis.csv
├── src/
│   ├── analyze_jobs.py
│   ├── analyze_skills.py
│   ├── check_salary_data.py
│   └── sql_analysis.py
├── joblens.db
└── README.md
```

## Current Dataset
- Original records: 97,929
- Duplicate records removed: 247
- Records after cleaning: 97,682
- Dataset columns: 17

## Current Findings
- Bengaluru has the largest number of listings in the analyzed dataset.
- Hyderabad and Pune are also among the leading locations.
- Application Developer and Application Lead are the most frequent job titles in the results.
- Python, SQL, SAP, Java, and Project Management appear frequently in the selected skill analysis.

## How to Run

Install the required libraries:

```bash
python -m pip install pandas openpyxl sqlalchemy
```

Run the scripts from the project root:

```bash
python src/analyze_jobs.py
python src/analyze_skills.py
python src/sql_analysis.py
python src/check_salary_data.py
```

## Important Data Limitations
- Salary values may be missing, inconsistent, or affected by parsing errors.
- Salary comparisons should be interpreted cautiously and are not guaranteed market-wide salary estimates.
- Skill counts are keyword-based and may not capture every variation of a skill.
- Findings describe this dataset, not every job available in India.

## Future Enhancements
- Build an interactive Power BI dashboard.
- Add more detailed skill categorization.
- Improve salary validation and normalization.
- Add experience-level and location-based comparisons.

## Project Status
**In progress** — data cleaning, skill analysis, and SQL-based analysis are implemented. Dashboard development and further validation are planned.