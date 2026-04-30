# Zomato Metro Analytics — Project Report

## 1. Cover Page
**Section:** D  
**Group:** G6  
**Members:**  
- Piyush Raj (Lead Data Analyst)  
- Shiva (Full Stack Developer)  
- Harshit (Data Engineer)  
- Pratyush Parida (Visualization Specialist)  

---

## 2. Executive Summary

**Problem:** Zomato lacks city-level visibility into the gap between dining and delivery experience across 13 Indian metro cities, making it difficult to prioritize delivery quality improvements.

**Approach:** Analyzed 1,23,657 menu-item-level records from Kaggle using a 7-step ETL pipeline, exploratory analysis, and statistical testing to surface actionable KPIs.

**Key Insights:**
- Delivery ratings are consistently higher than dining ratings across all 13 cities
- Pune has the largest dining-delivery gap (-0.355), followed by Bangalore (-0.279)
- BESTSELLER-tagged items receive ~10x more votes than untagged items
- Tea and Awadhi cuisines have the highest customer engagement by votes

**Key Recommendations:**
- Zomato should prioritize delivery quality improvements in Pune and Bangalore
- Best-seller tagging should be used strategically to boost engagement in low-vote cuisines

---

## 3. Sector and Business Context

**Sector:** Food-tech / Online food delivery

**Decision-maker:** Zomato city operations team

**Why this problem matters:** As Zomato expands delivery operations across Indian metros, understanding where delivery experience lags behind dine-in experience helps prioritize city-level interventions. A consistent delivery-dining gap signals systemic issues in logistics, packaging, or partner restaurant quality.

---

## 4. Problem Statement and Objectives

**Formal problem definition:** How can Zomato improve delivery performance and restaurant quality across 13 Indian metro cities to increase customer satisfaction and grow order volume?

**Scope:** 13 Indian metro cities — Hyderabad, Mumbai, Chennai, Jaipur, Bangalore, Ahmedabad, Kolkata, Pune, Kochi, Raipur, Lucknow, New Delhi, Goa.

**Success criteria:**
- Identify cities with the largest dining vs delivery rating gap (KPI-1)
- Identify cuisines with highest customer engagement by votes (KPI-2)
- Statistically validate findings with p-value < 0.05

---

## 5. Data Description

**Source:** Kaggle — narsingraogoud/zomato-restaurants-dataset-for-metropolitan-areas

**Access link:** https://www.kaggle.com/datasets/narsingraogoud/zomato-restaurants-dataset-for-metropolitan-areas

**Dataset size:** 1,23,657 rows (raw), 12 columns

**Granularity:** One row per menu item — each restaurant appears across multiple rows

**Key columns:** restaurant_name, dining_rating, delivery_rating, cuisine, city, votes, prices, best_seller

**Data quality issues:**
- 26.1% null values in dining_rating
- 1.0% null values in delivery_rating
- 22,127 duplicate rows from scraping
- Bangalore split into 4 locality names
- 95,715 null values in best_seller

---

## 6. Cleaning and Transformation

**Step 1 — Column normalization:** Fixed trailing space in "Cuisine " column name

**Step 2 — City normalization:** Merged Banaswadi, Ulsoor, Magrath Road, Malleshwaram into "Bangalore"

**Step 3 — Deduplication:** Removed 22,127 duplicate rows — raw 1,23,657 → clean 1,01,530

**Step 4 — Dining rating imputation:** Filled 26.1% nulls using City + Cuisine group median; fallback to city median

**Step 5 — Delivery rating imputation:** Filled 1% nulls using city-level median

**Step 6 — Best seller encoding:** Filled NaN with "None" — retained as categorical string

**Step 7 — Price outlier capping:** Clipped prices to [₹5, ₹3000] — no rows dropped

**Output dataset:** cleaned_zomato.csv — 1,01,530 rows, 12 columns

---

## 7. KPI Framework

| KPI | Definition | Formula | Why it matters |
|-----|-----------|---------|----------------|
| KPI-1 | Dining vs Delivery Rating Gap by City | dining_rating − delivery_rating per restaurant, averaged by city | Identifies which cities need the most delivery quality improvement |
| KPI-2 | Average Customer Votes per Cuisine | Mean of item-level votes grouped by cuisine | Identifies which cuisines drive the most customer engagement |
| KPI-3 | Best Seller Tag Impact on Votes | Mean votes for BESTSELLER vs untagged items | Validates whether best-seller tagging is a meaningful engagement signal |

---

## 8. Exploratory Analysis

*To be updated after EDA charts are finalized*

---

## 9. Statistical Analysis

**Method 1 — Paired t-test (KPI-1)**
- Compared dining_rating vs delivery_rating across all unique restaurants
- T-statistic: -10.79 | P-value: 0.000000
- Result: Significant difference between dining and delivery ratings

**Method 2 — One-way ANOVA (city-wise gap)**
- Tested whether rating gap differs significantly across 13 cities
- F-statistic: 3.31 | P-value: 0.000103
- Result: Rating gap is significantly different across cities — city-specific strategies are justified

**Method 3 — Welch t-test (KPI-3)**
- Compared votes for BESTSELLER-tagged vs untagged items
- Avg votes BESTSELLER: 82.4 | Avg votes untagged: 8.5 | P-value: 0.000000
- Result: BESTSELLER tag items have significantly more votes

---

## 10. Dashboard Walkthrough

*To be filled after Tableau dashboard is complete*

---

## 11. Key Insights

1. Delivery ratings are consistently higher than dining ratings across all 13 cities
2. Pune has the largest dining-delivery gap (-0.355) — highest priority for intervention
3. Bangalore has the second largest gap (-0.279)
4. Lucknow has the smallest gap (-0.033) — delivery and dining are nearly on par
5. Tea cuisine has the highest avg votes (761) — significantly ahead of all others
6. Awadhi cuisine is second (182 avg votes) — strong regional engagement
7. BESTSELLER-tagged items get ~10x more votes than untagged items (82.4 vs 8.5)
8. The dining-delivery gap is statistically significant (p < 0.05) across all cities
9. City-wise gap differences are statistically significant — one global strategy is insufficient
10. 13 cities covered with 1,01,530 clean records after removing scraping duplicates

---

## 12. Recommendations

1. **Prioritize Pune and Bangalore** for delivery quality improvement programs — both show gaps above -0.27
2. **Use best-seller tagging strategically** in low-engagement cuisines to boost visibility and order volume
3. **Investigate Tea and Awadhi cuisine popularity** — these cuisines show disproportionately high engagement and may represent expansion opportunities
4. **Replicate Lucknow's delivery model** in other cities — it has the smallest dining-delivery gap, suggesting effective delivery operations
5. **Run city-specific campaigns** — ANOVA confirms city gaps are statistically different, so a uniform national strategy will underperform

---

## 13. Limitations and Next Steps

**Data limitations:**
- Dataset is item-level, not order-level — actual delivery volumes are unknown
- 26.1% dining ratings were imputed — may introduce bias in gap calculations
- No timestamp data — trends over time cannot be analyzed

**Method limitations:**
- Correlation does not imply causation — rating gap drivers are not identified
- Best-seller tagging is platform-controlled, not restaurant-controlled

**Suggested future work:**
- Incorporate time-series data to track rating gap trends over quarters
- Add delivery time and complaint data for richer delivery quality analysis
- Expand to tier-2 cities for broader coverage

---

## 14. Contribution Matrix

| Member | Role | Contribution |
|--------|------|--------------|
| Piyush Raj | Lead Data Analyst | ETL Pipeline design, imputation logic, statistical analysis, and report writing. |
| Shiva | Full Stack Developer | Portfolio development, UI/UX design, and project documentation management. |
| Harshit | Data Engineer | Git version control, conflict resolution, and deployment orchestration. |
| Pratyush Parida | Visualization Specialist | Tableau dashboard design, dataset finding & cleaning, and report writing. |
