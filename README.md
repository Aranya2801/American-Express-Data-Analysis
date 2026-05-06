<p align="center">
  <img src="American_Express_logo_(2018).svg" width="180" alt="American Express Logo">
</p>

# 🏦 American Express — Data Intelligence Platform

### *A comprehensive, production-grade financial analytics suite for AXP (NYSE)*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-C6A84C?style=for-the-badge)](LICENSE)

---

> **10 years of American Express financial data (2016–2025) analyzed through advanced Python analytics, machine learning forecasting, and an interactive web dashboard — built for daily decision-making and portfolio intelligence.**

---

</div>

## 📌 Table of Contents

- [✨ Project Highlights](#-project-highlights)
- [📊 Dashboard Preview](#-dashboard-preview)
- [🗂️ Repository Structure](#️-repository-structure)
- [📦 Datasets Included](#-datasets-included)
- [🔬 Analysis Modules](#-analysis-modules)
- [🤖 Machine Learning](#-machine-learning)
- [📈 Key Findings](#-key-findings)
- [🚀 Quick Start](#-quick-start)
- [🛠️ Tech Stack](#️-tech-stack)
- [📅 Roadmap](#-roadmap)
- [🙋 About the Author](#-about-the-author)

---

## ✨ Project Highlights

<table>
<tr>
<td width="50%">

### 📐 What's Inside
- **10-year** historical dataset (FY2016 – FY2025)
- **Quarterly** granularity across 16 quarters
- **4 business segments** dissected individually
- **6-company** competitor benchmarking
- **ML revenue forecasting** through 2028
- **Interactive HTML dashboard** (zero backend required)
- **Live data fetch** via `yfinance` integration
- **Technical indicators**: RSI, MACD, Bollinger Bands

</td>
<td width="50%">

### 🎯 Use Cases
- 💼 **Daily portfolio tracking** for AXP holders
- 📚 **Research & learning** financial data analysis
- 📊 **Interview preparation** — showcase-ready project
- 🏫 **Academic** — case study on premium fintech
- 📉 **Risk analysis** — credit quality & write-offs
- 🔮 **Forecasting** — project 2026–2028 trajectory
- 🆚 **Competitive analysis** — vs Visa, MC, JPM, COF

</td>
</tr>
</table>

---

## 📊 Dashboard Preview

<div align="center">

### 🖥️ Interactive Web Dashboard
> Open `dashboard/index.html` in any browser — no server required.

| Section | Charts | Description |
|---------|--------|-------------|
| **Overview** | 5 charts | 10Y revenue, net income, EPS, margin, ROE |
| **Quarterly** | 4 charts | 16-quarter revenue, EPS, billed business, write-offs |
| **Segments** | 3 charts | Stacked revenue, pie mix, pretax margin |
| **Customers** | 5 charts | Cards, merchants, Gen Z, spending, premium mix |
| **Competitors** | 3 charts + table | Revenue, NPS, full benchmark table |
| **Forecast** | 2 charts | Poly regression + EPS forecast 2026–28 |

</div>

---

## 🗂️ Repository Structure

```
American-Express-Data-Analysis/
│
├── 📓 notebooks/
│   └── 01_Complete_Analysis.ipynb     ← Full 10-section analysis notebook
│
├── 📊 data/
│   ├── amex_annual_financials.csv     ← FY2016–2025 annual KPIs
│   ├── amex_quarterly_data.csv        ← 16 quarters of granular data
│   ├── amex_segments.csv              ← 4 business segments (2022–2025)
│   ├── amex_customer_metrics.csv      ← Demographics, spending, retention
│   └── competitor_analysis.csv        ← 6-company benchmark (2024–2025)
│
├── 🌐 dashboard/
│   └── index.html                     ← Fully interactive web dashboard
│
├── 🐍 src/
│   ├── amex_utils.py                  ← Shared analytics utilities
│   └── fetch_live_data.py             ← Live yfinance data refresh
│
├── 🖼️ assets/                         ← Auto-generated chart exports (PNG)
│   ├── kpi_scorecard.png
│   ├── financial_deep_dive.png
│   ├── quarterly_analysis.png
│   ├── segment_analysis.png
│   ├── customer_metrics.png
│   ├── competitor_analysis.png
│   └── ml_forecast.png
│
├── 📄 reports/
│   └── quick_summary.md               ← Auto-generated summary report
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📦 Datasets Included

### 1. `amex_annual_financials.csv` — 10-Year Annual Data
| Column | Description |
|--------|-------------|
| `Year` | Fiscal year (2016–2025) |
| `Total_Revenue_B` | Total net revenues ($B) |
| `Net_Income_B` | Net income attributable to AXP ($B) |
| `EPS_Diluted` | Diluted earnings per share ($) |
| `Billed_Business_T` | Card member billed business ($T) |
| `Cards_In_Force_M` | Total cards in force (millions) |
| `Net_Card_Fee_Revenue_B` | Net card fee revenue ($B) |
| `Net_Interest_Income_B` | Net interest income ($B) |
| `Return_on_Equity_pct` | Return on average equity (%) |
| `Stock_Price_EOY` | End-of-year stock price ($) |
| `Market_Cap_B` | Market capitalization ($B) |
| `Dividend_Per_Share` | Annual dividend per share ($) |
| `Credit_Loss_Provision_B` | Provisions for credit losses ($B) |

### 2. `amex_quarterly_data.csv` — Quarterly Granularity
16 quarters across 2022–2025 with revenue, EPS, billed business, new card acquisitions, card fees, NII, and write-off rates.

### 3. `amex_segments.csv` — Business Unit Breakdown
Revenue and pretax income for **US Consumer Services**, **Commercial Services**, **International Card Services**, and **GMNS & Other** — 2022 through 2025.

### 4. `amex_customer_metrics.csv` — Customer Intelligence
Demographics (Gen Z share, female cardholders), spending categories, retention rates, network reach, and credit quality metrics.

### 5. `competitor_analysis.csv` — Benchmarking
Side-by-side 2024–2025 data for **AXP, V, MA, JPM, COF, DFS** across revenue, net income, market cap, cards, purchase volume, NPS, and premium focus scores.

---

## 🔬 Analysis Modules

### Section 1 — Executive KPI Scorecard
> 8-metric color-coded dashboard comparing 2025 vs 2024 with directional arrows.

```python
# Metrics: Revenue, Net Income, EPS, Billed Business,
#          Cards In Force, Card Fees, Net Margin, ROE
```

### Section 2 — 10-Year Financial Deep Dive
```
📈 Dual-axis Revenue + Net Income bar/line chart
📊 Net Profit Margin trend (area fill)
💰 Diluted EPS growth bar chart
🎟️ Card Fee Revenue growth
📉 Return on Equity with 25% benchmark line
```

### Section 3 — Quarterly Trend Analysis
```
16 quarters · Revenue · EPS · Billed Business · Write-Off Rate
4-Quarter Moving Average overlays
Year-over-year color coding (2022 → 2025)
```

### Section 4 — Segment Deep Dive
```
Stacked bar: Revenue by segment (2022–2025)
Donut chart: 2025 revenue mix
Horizontal bar: Pretax margin by segment
```

### Section 5 — Customer & Network Intelligence
```
Cards in force growth
Merchant location expansion (99M → 160M)
Millennial / Gen Z acquisition trend
Spending category breakdown (6 categories)
Premium vs standard card mix evolution
```

### Section 6 — Competitive Benchmarking
```
Revenue comparison (6 companies)
Net Promoter Score comparison
Full 8-column benchmark table
```

### Section 7 — Correlation Heatmap
```
9×9 correlation matrix (lower-triangle heatmap)
Revenue vs Stock Price scatter with trend line
```

---

## 🤖 Machine Learning

### Revenue Forecasting (2026–2028)

Three models are fitted and evaluated:

| Model | R² Score | 2026 Forecast | 2027 Forecast | 2028 Forecast |
|-------|----------|---------------|---------------|---------------|
| **Linear Regression** | 0.9601 | $87.0B | $93.2B | $99.4B |
| **Polynomial (deg=3)** | **0.9984** | **$91B** | **$102B** | **$114B** |
| EPS Polynomial | 0.9971 | $17.2 | $19.1 | $21.3 |

> **Polynomial model recommended** — captures AXP's accelerating growth trajectory post-2022 premium card strategy shift.

### Technical Analysis (via `fetch_live_data.py`)
- **RSI-14** — Relative Strength Index (overbought / oversold signals)
- **MACD** — 12/26/9 Moving Average Convergence Divergence
- **Bollinger Bands** — 20-day with 2σ bands
- **50-day & 200-day Moving Averages**
- **30-day Rolling Volatility**

---

## 📈 Key Findings

### 💎 The Premium Card Strategy is Working
Net Card Fee Revenue grew from **$2.61B (2016)** to **$8.45B (2025)** — a **+224% increase** and the fastest-growing revenue line in the company. Fee revenue now represents **10.5% of total revenue**, up from 8.1% in 2016.

### 🧑‍💻 Gen Z Is the Future of AXP
**65% of new 2025 card acquisitions** came from Millennials and Gen Z — securing the next two decades of card member relationships. AXP has successfully repositioned from "old money" to "aspiration."

### 🌍 Network Parity Is Near
Merchant acceptance grew from ~80M locations in 2017 to **160M in 2025** — directly closing the long-standing network gap vs Visa and Mastercard that historically limited AXP.

### 📉 Best-in-Class Credit Quality
AXP's net write-off rate of **1.9% in 2025** remains significantly below Visa (N/A — network), Mastercard (N/A — network), and issuer peers Capital One (~5%) and Discover (~4.5%). The premium customer base acts as a structural credit quality shield.

### 💰 10-Year Revenue CAGR: ~10.8%
From $32.1B (2016) to $80.5B (2025), American Express has compounded revenue at ~10.8% annually — significantly outperforming most financial peers over the same period.

### 📊 ROE Trend
Return on Equity recovered from a 2020 COVID trough of **11.5%** to a 2025 high of **38.2%** — one of the highest ROEs in large-cap financial services globally.

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.10+
pip or conda
```

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/Aranya2801/American-Express-Data-Analysis.git
cd American-Express-Data-Analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Jupyter notebook
jupyter notebook notebooks/01_Complete_Analysis.ipynb
```

### Open the Dashboard
```bash
# Simply open in your browser — no server needed
open dashboard/index.html       # macOS
start dashboard/index.html      # Windows
xdg-open dashboard/index.html   # Linux
```

### Fetch Live Data
```bash
# Requires yfinance — pip install yfinance
python src/fetch_live_data.py
```

### Run Utilities
```python
from src.amex_utils import load_all_data, compute_annual_metrics, describe_financials

dfs = load_all_data(data_dir='data')
df  = compute_annual_metrics(dfs['annual'])
describe_financials(df)
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.10+ |
| **Data Wrangling** | Pandas 2.0, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Machine Learning** | Scikit-learn (Linear, Polynomial, Gradient Boosting) |
| **Statistics** | SciPy, StatsModels |
| **Live Data** | yFinance, pandas-datareader |
| **Dashboard** | Vanilla HTML5 + Chart.js 4.4 |
| **Notebooks** | Jupyter, ipywidgets |
| **Reporting** | OpenPyXL, ReportLab |

</div>

---

## 📅 Roadmap

- [x] 10-year annual dataset (2016–2025)
- [x] Quarterly granularity (2022–2025)
- [x] 4-segment breakdown
- [x] Customer & network metrics
- [x] 6-company competitor benchmark
- [x] ML revenue & EPS forecasting
- [x] Interactive HTML dashboard (6 tabs, 20+ charts)
- [x] Live data fetch via yfinance
- [x] Technical indicators (RSI, MACD, Bollinger)
- [ ] Streamlit interactive web app
- [ ] Monte Carlo simulation for stock price
- [ ] NLP sentiment analysis on earnings call transcripts
- [ ] Automated PDF report generation
- [ ] Docker containerization
- [ ] GitHub Actions CI/CD pipeline

---

## 📄 Data Sources

| Source | Usage |
|--------|-------|
| [American Express Investor Relations](https://ir.americanexpress.com) | Official annual reports & earnings releases |
| [SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=AXP) | 10-K and 10-Q filings |
| [MacroTrends](https://www.macrotrends.net/stocks/charts/AXP/american-express) | Historical financial data |
| [yFinance](https://pypi.org/project/yfinance/) | Live stock price & fundamentals |
| [Statista](https://www.statista.com) | Card industry benchmarks |

> ⚠️ *This project is for educational and analytical purposes only. It does not constitute financial advice.*

---

## 🙋 About the Author

<div align="center">

**Aranya2801**

[![GitHub](https://img.shields.io/badge/GitHub-Aranya2801-181717?style=for-the-badge&logo=github)](https://github.com/Aranya2801)

*Built with passion for data, finance, and beautiful analytics.*

---

⭐ **If this project helped you, please give it a star!** ⭐

</div>

---

<div align="center">
<sub>© 2025 Aranya2801 · MIT License · American Express® is a registered trademark of American Express Company. This project is an independent analytical work and is not affiliated with or endorsed by American Express Company.</sub>
</div>

