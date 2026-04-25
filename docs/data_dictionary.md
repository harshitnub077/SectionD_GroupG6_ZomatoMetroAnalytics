# Data Dictionary
## Zomato Restaurants Dataset for Metropolitan Areas

---

## Dataset Summary

| Item | Details |
|------|---------|
| Dataset name | Zomato Restaurants Dataset for Metropolitan Areas |
| Source | Kaggle — narsingraogoud/zomato-restaurants-dataset-for-metropolitan-areas |
| Raw file name | zomato_dataset.csv |
| Processed file name | cleaned_zomato.csv |
| Tableau-ready file | tableau_ready_zomato.csv |
| Raw row count | 1,23,657 |
| Cleaned row count | 1,01,530 |
| Column count | 12 |
| Granularity | One row per menu item — each restaurant appears across multiple rows |
| Cities covered | 13 — Hyderabad, Mumbai, Chennai, Jaipur, Bangalore, Ahmedabad, Kolkata, Pune, Kochi, Raipur, Lucknow, New Delhi, Goa |
| Last updated | April 2026 |

---

## Column Definitions

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|-------------|-----------|-------------|---------------|---------|----------------|
| restaurant_name | string | Name of the restaurant on Zomato | Doner King | EDA, KPI-1, Tableau | Whitespace stripped |
| dining_rating | float | Customer rating for dine-in experience (1.0–5.0) | 3.9 | EDA, KPI-1, Stats | 26.1% nulls — imputed using City+Cuisine median, fallback to city median |
| delivery_rating | float | Customer rating for delivery experience (1.0–5.0) | 4.2 | EDA, KPI-1, Stats | 1.0% nulls — imputed using city-level median |
| dining_votes | Int64 | Number of votes cast for dining experience | 39 | EDA, Stats | Cast from object to Int64 |
| delivery_votes | Int64 | Number of votes cast for delivery experience | 0 | EDA, Stats | Zero is valid — not treated as null |
| cuisine | string | Primary cuisine type of the restaurant | Fast Food | EDA, KPI-2, Tableau | Raw column had trailing space "Cuisine " — fixed by str.strip() |
| place_name | string | Locality or neighbourhood within the city | Malakpet | Tableau | Whitespace stripped |
| city | string | Metro city where restaurant is located | Hyderabad | EDA, KPI-1, Stats, Tableau | Banaswadi, Ulsoor, Magrath Road, Malleshwaram remapped to Bangalore |
| item_name | string | Name of the specific menu item | Platter Kebab Combo | EDA, KPI-2 | Whitespace stripped |
| best_seller | string | Zomato-assigned promotional tag for the item | BESTSELLER | EDA, KPI-3, Tableau | NaN filled with "None" — 13 distinct tag values retained as categories |
| votes | Int64 | Number of customer votes for that specific menu item | 84 | EDA, KPI-2, KPI-3, Stats | Cast from object to Int64 |
| prices | float | Listed price of the menu item in INR | 249.0 | EDA, KPI-5, Tableau | Cast to float — clipped to [5, 3000] to handle outliers |

---

## Derived Columns

| Derived Column | Logic | Business Meaning |
|----------------|-------|-----------------|
| rating_gap | dining_rating − delivery_rating per restaurant | KPI-1 — positive value means dine-in rated better than delivery. Cities with high gap need targeted delivery improvement |
| avg_item_votes | Mean of votes grouped by cuisine using transform | KPI-2 — identifies which cuisines attract highest per-item customer engagement |

---

## Data Quality Notes

- **22,127 duplicate rows** found in raw data from scraping — removed using drop_duplicates()
- **26.1% null dining ratings** — not dropped to preserve row count; imputed using City+Cuisine group median
- **1.0% null delivery ratings** — imputed using city-level median
- **Bangalore fragmented** into 4 locality names (Banaswadi, Ulsoor, Magrath Road, Malleshwaram) — all remapped to "Bangalore"
- **best_seller had 95,715 NaN values** — NaN means no tag assigned, filled with "None" to make it a valid category
- **Price outliers** — 60 items below ₹5 and 29 items above ₹3,000 — clipped to [5, 3000], no rows dropped
- **Dataset is item-level not restaurant-level** — dining_rating and delivery_rating repeat across all items of a restaurant; KPI-1 uses drop_duplicates(subset=["restaurant_name", "city"]) before aggregating
