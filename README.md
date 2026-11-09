# Tata Motors Stock Market Data Analysis (2000–2025)

## Project Overview

This project explores historical Tata Motors stock market data from 2000 to 2025 using Python. It focuses on data cleaning, exploratory data analysis, statistical analysis and financial data visualization to identify historical stock price trends, returns, volatility and market patterns.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Yahoo Finance API (`yfinance`)
- Jupyter Notebook

## Project Objectives

- Collect historical Tata Motors stock market data.
- Clean and preprocess financial datasets.
- Analyze historical stock price movements.
- Calculate daily and annual returns.
- Study moving averages and volatility.
- Identify maximum historical drawdown.
- Analyze monthly performance and variable correlations.
- Generate meaningful financial visualizations.

## Dataset Information

| Attribute | Details |
|---|---|
| Company | Tata Motors |
| Historical period | 2000–2025 |
| Initial ticker used | TMPV.NS |
| Data source | Yahoo Finance |
| Initial records downloaded | 6,488 |
| Frequency | Daily |

The dataset includes Open, High, Low, Close, Adjusted Close and Volume.

**Data consideration:** Tata Motors underwent a demerger in 2025. The historical ticker lineage and corporate-action adjustments must be considered when interpreting the data.

## Project Structure

```text
Tata-Motors-Stock-Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── tata_motors_analysis.ipynb
│
├── src/
│   ├── data_collection.py
│   ├── data_cleaning.py
│   └── analysis_summary.py
│
├── outputs/
│   ├── charts/
│   ├── annual_risk_return.csv
│   └── final_analysis_report.txt
│
├── requirements.txt
└── README.md
```

## Analysis Performed

### 1. Data Collection
Downloaded historical stock market data using Yahoo Finance.

### 2. Data Cleaning
- Missing value checks
- Duplicate record removal
- Data validation
- Date sorting
- Feature engineering

### 3. Exploratory Data Analysis
- Historical stock price trends
- Moving average analysis
- Annual stock returns
- Trading volume analysis
- Daily return distribution

### 4. Advanced Financial Analysis
- Monthly returns heatmap
- Rolling volatility
- Maximum drawdown
- Correlation matrix
- Annual risk and return analysis

## Key Performance Indicators

- Historical adjusted-price return
- Best and worst annual returns
- Average daily return
- Annualized volatility
- Maximum drawdown
- Average trading volume

## How to Run the Project

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project:

```bash
cd Tata-Motors-Stock-Analysis
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Collect the data:

```bash
python src/data_collection.py
```

Clean the data:

```bash
python src/data_cleaning.py
```

Generate the summary:

```bash
python src/analysis_summary.py
```

Open the Jupyter Notebook:

```bash
jupyter notebook
```

## Project Outcomes

This project demonstrates practical skills in Python programming, financial data manipulation, exploratory data analysis, statistical calculations and data visualization.

## Disclaimer

This project is intended for educational and analytical purposes only. Historical stock performance does not guarantee future returns. It is not investment advice.
