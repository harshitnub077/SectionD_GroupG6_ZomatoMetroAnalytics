# ShopLens — Zomato Metro Restaurant Analytics

> **Newton School of Technology · Data Visualization & Analytics · Capstone 2**
> Decoding dining patterns, rating gaps, and price intelligence across 13 Indian metropolitan cities.

---

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | ShopLens — Zomato Metro Restaurant Analytics |
| **Sector** | Food-Tech & Restaurant Analytics |
| **Team ID** | G-6 |
| **Section** | Section D |
| **Faculty Mentor** | Archit Raj |
| **Institute** | Newton School of Technology |
| **Submission Date** | April 2026 |

### Team Members

| Role | Name |
|---|---|
| Project Lead | Shiva Sharma |
| Data Engineer | Harshit Kudhial |
| Statistical Analyst | Phalak Sharma |
| Visualization Specialist | Pratyush Parida |
| Research & QA | Piyush Raj |
| Documentation Lead | S. Shiva Sankar M. K. |

---

## Business Problem

India's food delivery and dining-out market has reached saturation in several metro cuisine categories. Simply opening a restaurant in a high-footfall area is no longer enough — operators need data-driven visibility into cuisine-level demand, city-specific pricing tolerance, and the performance gap between dine-in and delivery experiences.

The rating divergence between delivery and dining is an underexplored operational risk. A restaurant that performs well on delivery but poorly in-person may sustain short-term revenue through aggregator platforms, but risks long-term brand erosion as dine-in reviews suppress overall visibility scores on discovery platforms like Zomato.

**Core Business Question**

> How can Zomato restaurant operators and market analysts identify city-level rating gaps, cuisine-specific performance disparities, and price-to-quality misalignments across Indian metropolitan areas — to improve restaurant positioning and customer satisfaction?

**Decision Supported**

> Enables Zomato operators and restaurant chains to make data-backed decisions on city market entry, cuisine selection risk, and pricing strategy — reducing early-stage rating failures and improving repeat order rates.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source** | Zomato Restaurants Dataset — Metropolitan Areas (Kaggle) |
| **Direct Link** | [kaggle.com/datasets/narsingraogoud/zomato-restaurants-dataset-for-metropolitan-areas](https://www.kaggle.com/datasets/narsingraogoud/zomato-restaurants-dataset-for-metropolitan-areas) |
| **Raw Row Count** | 1,23,657 |
| **Cleaned Row Count** | 1,01,530 |
| **Column Count** | 12 |
| **Unique Restaurants** | 826 |
| **Cities Covered** | 13 |
| **Format** | CSV |

### Cities Covered

`Ahmedabad` · `Bangalore` · `Chennai` · `Goa` · `Hyderabad` · `Jaipur` · `Kochi` · `Kolkata` · `Lucknow` · `Mumbai` · `New Delhi` · `Pune` · `Raipur`

### Key Columns

| Column | Description | Role in Analysis |
|---|---|---|
| `dining_rating` | Customer rating for dine-in experience (1.0–5.0) | Primary KPI — city/cuisine segmentation |
| `delivery_rating` | Customer rating for delivery experience (1.0–5.0) | Primary KPI — gap analysis |
| `cuisine` | Primary cuisine type of the restaurant | Segmentation and heatmap filter |
| `city` | Metro city where the restaurant is located | City-level grouping and ANOVA |
| `prices` | Listed price of the menu item in INR | Price tier classification and correlation |
| `best_seller` | Zomato-assigned promotional tag for the item | Engagement and visibility filter |
| `votes` | Number of customer votes per menu item | Popularity weighting |
| `rating_gap` *(derived)* | `dining_rating − delivery_rating` per restaurant | Core KPI — negative = dining underperforms |

For full column definitions and cleaning notes, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Value | Interpretation |
|---|---|---|
| **Avg Dining Rating** | 3.827 | Solid baseline; room for improvement in dine-in service quality |
| **Avg Delivery Rating** | 3.959 | Delivery experience outperforms dine-in consistently across all 13 cities |
| **Avg Rating Gap** | −0.1321 | Negative gap = dining consistently scores lower than delivery (statistically significant, p < 0.001) |
| **Avg Item Price** | ₹243.4 | Mid-range positioning; significant city-level variance exists |
| **Total Restaurants** | 826 | Analytical universe for all rate-based and segment metrics |
| **Cities Covered** | 13 | All major Indian metropolitan areas represented |

KPI computation logic is documented in [`notebooks/04_statistical_analysis.ipynb`](notebooks/04_statistical_analysis.ipynb) and [`notebooks/05_final_load_prep.ipynb`](notebooks/05_final_load_prep.ipynb).

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard 1 — Zomato Metro Analytics** | KPI tiles + Avg Dining Rating bar chart + City map · *Audience: Operations* |
| **Dashboard 2 — Zomato Rating Analytics** | City-Cuisine heatmap + Scatter plot + Rating gap histogram · *Audience: Strategy* |
| **Dashboard 3 — Menu Price Analytics** | Avg Item Price by Cuisine + Price Tier Distribution by City · *Audience: Pricing* |
| **Main Filters** | City · Cuisine |

Dashboard screenshots are stored in [`tableau/screenshots/`](tableau/screenshots/). Public links are documented in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights

1. **Delivery consistently outperforms dining.** The −0.1321 average rating gap is statistically significant (p < 0.001), confirming a structural dine-in service quality problem — not random variation — across all 13 cities.

2. **Raipur beats every major metro.** With the highest average dining rating in the dataset, Raipur outperforms Mumbai, Bangalore, and New Delhi. Lower restaurant density means less quality dilution.

3. **Goa is a delivery outlier.** High dining ratings but below-average delivery ratings — the inverse of the national trend. Geographic and logistics constraints likely prevent Goa restaurants from replicating their in-person experience through delivery.

4. **Sichuan carries the highest rating volatility.** The City-Cuisine heatmap shows Sichuan with the most inconsistent gaps across cities — high sensitivity to local ingredient availability and chef expertise makes it the highest-risk expansion category.

5. **Higher price ≠ higher rating.** Pearson correlation between price and dining rating is weak (r ≈ 0.18), explaining less than 4% of rating variance. Restaurants pricing above ₹243.4 without a corresponding rating premium risk negative value perception.

6. **Dangerous outliers exist in the rating gap distribution.** The histogram reveals a long left tail extending to −1.6 — restaurants where the dine-in experience dramatically underperforms delivery. These are disproportionately likely to generate negative word-of-mouth.

7. **Beverages and Shakes are the lowest-risk cuisine categories.** Minimal cooking complexity and standardised recipes translate directly into consistent customer experience across all 13 cities.

8. **Pune is the most operationally balanced city.** High on both dining and delivery rating axes — the lowest-risk environment for piloting new restaurant formats or testing new cuisines.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Systemic dining-delivery gap | Audit the bottom 20% of restaurants by dining rating in each city; mandate service reviews covering wait times, staff training, and ambience. Set a minimum dining rating floor of 3.7 before premium price tier listing. | +0.1 avg dining rating → ~75% closure of the dining-delivery gap |
| 2 | Price-rating misalignment in Goa & Ahmedabad | Publish city-level pricing benchmarks by cuisine and price tier. Flag restaurants pricing >25% above city-cuisine median without a matching rating premium for automated pricing review. | 10–15% improvement in repeat order rates in affected cities |
| 3 | Sichuan and niche cuisine volatility | Classify cuisines into Low Risk (Beverages, Shakes, Fast Food), Medium Risk (Chinese, Biryani, Pizza), and High Risk (Sichuan, Desserts in specific cities). Surface this classification during new restaurant onboarding. | Reduced early-stage negative rating events for new restaurants |
| 4 | Raipur-tier cities outperform saturated metros | Shift incremental marketing and restaurant acquisition budget toward high-rating smaller cities over Bangalore-tier markets. | +20% restaurant count in quality-vetted smaller cities at lower CAC than saturated metros |

---

## Statistical Analysis

Three tests were run to validate EDA findings:

| Test | Groups Compared | Result | Conclusion |
|---|---|---|---|
| **Paired T-Test** | Dining vs. Delivery Rating | Mean diff = −0.132, p < 0.001 | Delivery rating is significantly and consistently higher |
| **One-Way ANOVA** | Dining Rating across 13 cities | F-statistic significant, p < 0.05 | City is a meaningful predictor of dining rating |
| **Pearson Correlation** | Price vs. Dining Rating | r ≈ 0.18, p < 0.05 | Weak positive — premium price does not guarantee premium experience |

---

## Repository Structure

```text
SectionD_G6_ZomatoMetroAnalytics/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   └── zomato_dataset.csv            # Original dataset (never edited)
│   └── processed/
│       ├── cleaned_zomato.csv            # Output of cleaning pipeline
│       └── tableau_ready_zomato.csv      # Aggregated, Tableau-optimised export
│
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
│
├── scripts/
│   └── etl_pipeline.py
│
├── tableau/
│   ├── screenshots/
│   └── dashboard_links.md
│
├── reports/
│   ├── Zomato_Report_G6_FINAL.pdf
│   └── Zomato_Analytics_Dashboard_Capstone2.pdf
│
├── docs/
│   └── data_dictionary.md
│
├── DVA-Oriented-Resume/
└── DVA-Focused-Portfolio/
```

---

## Analytical Pipeline

1. **Define** — Sector scoped, problem statement approved by faculty mentor Archit Raj.
2. **Extract** — Raw dataset sourced from Kaggle and committed to `data/raw/`; data dictionary drafted in `docs/`.
3. **Clean & Transform** — ETL pipeline built in `notebooks/02_cleaning.ipynb`: null imputation, feature engineering (`rating_gap`, `price_tier`), cuisine standardisation, Bangalore locality remapping.
4. **Analyse** — EDA and statistical analysis in `notebooks/03_eda.ipynb` and `04_statistical_analysis.ipynb`; Paired T-Test, ANOVA, and Pearson Correlation.
5. **Visualise** — Three Tableau dashboards (Operations, Strategy, Pricing) built and published on Tableau Public.
6. **Recommend** — Four data-backed business recommendations with projected impact estimates.
7. **Report** — Final report and presentation deck exported to PDF in `reports/`.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python + Jupyter Notebooks | ETL, data cleaning, EDA, KPI computation, statistical testing |
| Pandas · NumPy · Matplotlib · Seaborn · SciPy | Core Python libraries |
| Tableau Public | Interactive dashboard design, publishing, and sharing |
| GitHub | Version control and collaboration |

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/harshitnub077/SectionD_GroupG6_ZomatoMetroAnalytics.git
cd SectionD_G6_ZomatoMetroAnalytics

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run notebooks in order
jupyter notebook
```

If using Google Colab, upload or sync notebooks from `notebooks/` and export cleaned datasets back to `data/processed/`.

---

## Contribution Matrix

| Team Member | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
|---|---|---|---|---|---|---|---|
| Shiva Sharma | Support | Support | Support | **Owner** | Support | Support | Support |
| Harshit Kudhial | **Owner** | **Owner** | Support | Support | Support | Support | Support |
| Phalak Sharma | Support | Support | Support | Support | Support | **Owner** | **Owner** |
| Pratyush Parida | **Owner** | Support | **Owner** | Support | Support | **Owner** | Support |
| Piyush Raj | **Owner** | Support | Support | Support | Support | **Owner** | Support |
| S. Shiva Sankar M. K. | Support | Support | Support | Support | **Owner**| **Owner** | **Owner** |

---

## Limitations & Future Scope

**Current Limitations**
- The 826-restaurant sample is sufficient for city-level findings but too small for high-confidence cuisine-level subgroup analysis, particularly for niche categories like Sichuan.
- No time-series order data — seasonal patterns and trend analysis are not currently possible.
- Dataset is a snapshot, not a live feed — findings are valid for the period covered but may shift as Zomato's restaurant mix evolves.

**Future Scope**
- Expand dataset to include order volume and revenue data for GMV-based analysis.
- Integrate time-series data for seasonal demand forecasting by cuisine and city.
- Build a real-time Tableau integration to convert retrospective dashboards into live monitoring tools that alert managers to emerging rating gaps before they compound.

---

*Newton School of Technology · Data Visualization & Analytics · Capstone 2 · April 2026*
