# Zomato Metro Analytics: A Closer Look at Metropolitan Area Food Culture

Welcome to the **Zomato Metro Analytics** project by **Section D, Group G6**. 

This repository analyzes the [Zomato Restaurants Dataset for Metropolitan Areas](https://www.kaggle.com/datasets/narsingraogoud/zomato-restaurants-dataset-for-metropolitan-areas), diving deep into the food culture, pricing, restaurant performance, and culinary variety across major Indian cities. Our goal is to extract actionable insights through robust Data Visualisation and Analytics (DVA).

## 🚀 ETL Pipeline & Data Cleaning (Notebook 02)

To ensure high-quality analysis, we implemented a rigorous ETL (Extract, Transform, Load) pipeline in our primary data preparation phase (Notebook 02). The dataset had several raw scraping artifacts, formatting issues, and missing values.

We have locked in the following **7 documented transformation steps** to establish a clean, reliable, and perfectly formatted dataset:

1. **Standardize Column Names:** 
   - `df.columns = df.columns.str.strip()` — Fixed a pesky trailing space bug (e.g., `"Cuisine "` → `"Cuisine"`).
2. **City Normalization:** 
   - `df['City'] = df['City'].str.strip()` followed by remapping 4 fragmented Bangalore localities into a unified `"Bangalore"` category.
3. **Deduplication:** 
   - `df.drop_duplicates()` — Successfully removed 22,127 redundant scraping duplicates.
4. **Targeted Dining Rating Imputation:** 
   - Imputed null `Dining Rating` values using the median, strategically grouped by `City` + `Cuisine` to maintain local culinary context.
5. **Targeted Delivery Rating Imputation:** 
   - Imputed null `Delivery Rating` values with the overall city-level median.
6. **Feature Engineering (Best Seller):** 
   - Cleaned the `Best Seller` column by filling `NaN` values with `"None"` and retaining only meaningful tags.
7. **Outlier Capping (Prices):** 
   - Handled extreme pricing anomalies by flagging and capping anything below ₹5 or excessively high prices above ₹3,000.

Every issue addressed in this pipeline is real, verifiable via `df.isnull().sum()`, and solved using standard, highly optimized `pandas` code. 

## 📂 Project Structure

- `data/`: Contains the raw and processed Zomato datasets.
- `notebooks/`: Jupyter notebooks detailing EDA, ETL (Pipeline 02), and model building.
- `scripts/`: Modular Python scripts for reusable data processing tasks.
- `tableau/`: Workbooks and visual assets for the dashboard presentation.
- `reports/`: Documentation and analytical findings.
- `docs/`: Supporting project literature.
- `DVA-Focused-Portfolio/` & `DVA-Oriented-Resume/`: Team member portfolios and related documents.

## 🛠️ Tech Stack

- **Data Processing:** Python, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Tableau
- **Environment:** Jupyter Notebooks

---
*Created for the Data Visualisation and Analytics evaluation.*