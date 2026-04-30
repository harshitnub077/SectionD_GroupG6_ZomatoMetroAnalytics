> ■■■■■■■■■■■■■■■■■■■■■■■■■
>
> *Decoding Dining Patterns, Rating Gaps & Price Intelligence across 13
> Indian Metropolitan Cities*
>
> ■■■■■■■■■■■■■■■■■■■■■■■■■

+-----------------+----------------+-----------------+----------------+
| **826**         | **13**         | **3.827**       | > **₹243.4**   |
|                 |                |                 | >              |
| Total           | Cities Covered | Avg Dining      | > Average      |
| Restaurants     |                | Rating          | > Price        |
+=================+================+=================+================+
+-----------------+----------------+-----------------+----------------+

+-----------------+----------------------------------------------------+
| > **Sector**    | > Food-Tech & Restaurant Analytics                 |
+=================+====================================================+
| > **Dataset**   | > Zomato Restaurants --- Metropolitan Areas        |
|                 | > (Kaggle)                                         |
+-----------------+----------------------------------------------------+
| > **Tools**     | > Python (Pandas) · Tableau · Statistical Testing  |
+-----------------+----------------------------------------------------+
| > **Date**      | > April 2026                                       |
+-----------------+----------------------------------------------------+
| > **Institute** | > Newton School of Technology                      |
+-----------------+----------------------------------------------------+
| > **Faculty     | > Archit Raj                                       |
| > Mentor**      |                                                    |
+-----------------+----------------------------------------------------+
| > **Team**      | > Team G-6 \| Section D                            |
+-----------------+----------------------------------------------------+

  -----------------------------------------------------------------------
  **Team Member**        **Role**         **Primary Focus**
  ---------------------- ---------------- -------------------------------
  Shiva Sharma           Project Lead     Hypothesis Testing & KPIs

  Harshit Kudhial        Data Engineer    ETL Pipeline & Data Cleaning

  Phalak Sharma          Statistical      Presentation & Data Cleaning
                         Analyst          

  Pratyush Parida        Visualization    Dashboard Design & Report
                         Specialist       

  Piyush Raj             Research & QA    Dataset Validation & Insights

  S. Shiva Sankar M. K.  Documentation    Report Writing & References
                         Lead             
  -----------------------------------------------------------------------

> ShopLens is a data analytics initiative designed to extract
> operational and strategic insights from Zomato\'s restaurant data
> across India\'s major metropolitan areas. The project was executed on
> a dataset of 1,23,657 rows spanning 826 unique restaurants across 13
> cities, using a Python-based ETL pipeline, Tableau dashboards, and
> rigorous statistical analysis.
>
> The analysis surfaces three mission-critical findings that directly
> impact restaurant positioning strategy, cuisine pricing decisions, and
> city-level market entry planning for food-tech operators and
> restaurant chains.

#  The Three Core Findings  {#the-three-core-findings .unnumbered}

> India\'s food delivery and dining-out market has undergone a
> structural transformation over the past decade. Zomato, currently
> serving over 500 cities and processing millions of orders daily,
> operates as both a discovery platform and a logistics network ---
> making its data a proxy for the broader health of India\'s restaurant
> economy.
>
> With restaurant density in metro cities reaching saturation in certain
> cuisine categories, operators face a new challenge: it is no longer
> sufficient to simply open a restaurant in a high-footfall area.
> Success now depends on understanding cuisine-level demand,
> city-specific pricing tolerance, and the gap between dine-in and
> delivery experience quality.
>
> The rating gap between delivery and dining experiences is an
> underexplored operational risk. A restaurant that performs well on
> delivery but poorly in-person may sustain short-term revenue through
> aggregator platforms, but risks long-term brand erosion as dine-in
> reviews suppress overall visibility scores.
>
> Price positioning is equally critical. An average item price of ₹243.4
> across the dataset masks significant city- level variance. In markets
> where customers have high price sensitivity, even a modest premium
> over competitors can trigger abandonment. Without data-driven
> visibility into how price tiers correlate with ratings by city,
> restaurant owners set pricing based on intuition rather than market
> evidence.

#  Research Question  {#research-question .unnumbered}

> The primary dataset is the Zomato Restaurants Dataset for Metropolitan
> Areas, sourced from Kaggle. It contains restaurant-level records from
> Zomato\'s platform, covering 13 major Indian cities with detailed
> information on cuisines, ratings (both dining and delivery), pricing,
> votes, and best-seller items.

1.  **[​Dataset Specifications]{.underline}**

  -----------------------------------------------------------------------
  **Attribute**         **Details**
  --------------------- -------------------------------------------------
  Source                Zomato Restaurants Dataset --- Metropolitan Areas
                        (Kaggle)

  Total Rows            1,23,657 restaurant-level records

  Total Restaurants     826 unique restaurants

  Cities Covered        13 Indian metropolitan cities

  Key Columns           Restaurant Name, City, Cuisine, Dining Rating,
                        Delivery Rating, Prices, Votes

  Derived Fields        Rating Gap (Delivery − Dining), Above/Below
                        Average flag, Price Tier

  Data Quality Issues   Missing delivery ratings; inconsistent cuisine
                        label formatting; null best- seller values
  -----------------------------------------------------------------------

2.  **[​Cities Covered]{.underline}**

  -----------------------------------------------------------------------
  Ahmedabad   Bangalore   Chennai     Goa         Hyderabad   Jaipur
  ----------- ----------- ----------- ----------- ----------- -----------
  Kochi       Kolkata     Lucknow     Mumbai      New Delhi   Pune

  Raipur                                                      
  -----------------------------------------------------------------------

3.  **[​Limitations]{.underline}**

> Two important limitations should be noted. First, the dataset covers
> 826 restaurants across 13 cities --- a meaningful sample but not fully
> representative of each city\'s complete restaurant ecosystem. Second,
> the dataset does not include time-series order volumes or revenue
> figures, meaning all financial impact estimates in this report are
> directional proxies rather than institution-specific actuals.
>
> The project employed a three-stage Python ETL pipeline built on the
> Pandas library, processing the raw Zomato CSV into a single unified
> analytical master dataset.

+-----------------------+-----------------------+-----------------------+
| **Stage 1**           | **Stage 2**           | **Stage 3**           |
|                       |                       |                       |
| **EXTRACTION**        | **TRANSFORMATION**    | **LOAD**              |
+=======================+=======================+=======================+
+-----------------------+-----------------------+-----------------------+

> **Stage 1 --- Extraction**
>
> The raw CSV file was ingested into a Pandas DataFrame. Initial
> profiling identified column types, null distributions, and value
> cardinalities. Key fields inspected included Dining Rating, Delivery
> Rating, Prices, City, and Cuisine --- all of which exhibited varying
> degrees of null values and formatting inconsistencies.
>
> **Stage 2 --- Transformation**
>
> Null handling was the first priority. Rows with missing values in the
> Dining Rating and Delivery Rating columns were flagged and either
> imputed with city-level medians or removed where no reliable
> imputation was possible. Feature engineering followed:

-   Rating Gap computed as Delivery Rating minus Dining Rating ---
    negative values indicate dining underperformance.

-   Above/Below Average flag derived by comparing each restaurant\'s
    Dining Rating against the city- level mean.

-   Price Tier classification applied using quartile-based binning into
    Budget, Mid-Range, Premium, and Luxury tiers.

-   Cuisine standardisation performed to merge variant spellings into
    consistent labels across all 13 cities.

> **Stage 3 --- Load**
>
> The cleaned master dataset was exported as tableau_ready_zomato.csv
> for archival and reproducibility. Aggregated subset files ---
> pre-grouped by city, cuisine, and price tier --- were exported
> separately as Tableau- optimised ingestion files, ensuring dashboard
> rendering performance remained responsive across all filter
> combinations.
>
> Six core KPIs were computed and validated against the cleaned dataset.
> Each metric is described below with its operational interpretation.

+-----------------+----------------+-----------------+----------------+
| **3.827**       | **3.959**      | > **-0.1321**   | > **₹243.4**   |
|                 |                | >               | >              |
| Avg Dining      | Avg Delivery   | > Avg Rating    | > Avg Item     |
| Rating          | Rating         | > Gap           | > Price        |
+=================+================+=================+================+
+-----------------+----------------+-----------------+----------------+

+--------------------+---------+--------------------------------------+
| **KPI**            | > **    | **Operational Interpretation**       |
|                    | Value** |                                      |
+====================+=========+======================================+
| Avg Dining Rating  | 3.827   | Solid baseline; room for improvement |
|                    |         | in dine-in service quality           |
+--------------------+---------+--------------------------------------+
| Avg Delivery       | 3.959   | Delivery experience outperforms      |
| Rating             |         | dine-in consistently across cities   |
+--------------------+---------+--------------------------------------+
| Avg Rating Gap     | -0.1321 | Negative gap = dining consistently   |
|                    |         | scores lower than delivery           |
+--------------------+---------+--------------------------------------+
| Avg Item Price     | ₹243.4  | Mid-range positioning; significant   |
|                    |         | city-level variance exists           |
+--------------------+---------+--------------------------------------+
| Total Restaurants  | 826     | Analytical universe for all          |
|                    |         | rate-based and segment metrics       |
+--------------------+---------+--------------------------------------+
| Cities Covered     | 13      | All major Indian metropolitan areas  |
|                    |         | represented in dataset               |
+--------------------+---------+--------------------------------------+

> Exploratory analysis proceeded from macro KPI profiling to city-level
> and cuisine-level decomposition. The Tableau dashboard architecture
> --- split across two dashboards --- drove the primary EDA conclusions.

#  ​Average Dining Rating by City 

> The horizontal bar chart reveals that Raipur, Pune, New Delhi, and
> Hyderabad post dining ratings at or above the dataset average of
> 3.827, while Bangalore, Chennai, and Ahmedabad consistently fall
> below. This is counterintuitive --- larger, more competitive markets
> like Bangalore score lower than smaller metro markets like Raipur,
> suggesting competition density dilutes average quality.
>
> **Average Dining Rating by City (vs. Overall Average: 3.827)**
>
> ██████████████████████████████
>
> ██████████████████████████████
>
> █████████████████████████████
>
> █████████████████████████████
>
> █████████████████████████████
>
> █████████████████████████████
>
> █████████████████████████████
>
> █████████████████████████████
>
> █████████████████████████████
>
> █████████████████████████████
>
> ████████████████████████████
>
> ████████████████████████████
>
> ████████████████████████████

#  ​Dining vs. Delivery Rating Comparison 

> The scatter plot maps each city on axes of Average Dining Rating (X)
> vs. Average Delivery Rating (Y), with an \'Equal Ratings\' reference
> line. Cities above the line have delivery ratings exceeding dining
> ratings. The analysis shows virtually all cities sit above the
> equal-ratings line --- confirming the systemic delivery advantage.
> Pune emerges as the most balanced city for restaurant operations.

+---------------+--------------+--------------+---------+------------+
| **City**      | **Avg        | **Avg        | **Gap** | > **       |
|               | Dining**     | Delivery**   |         | Position** |
+===============+==============+==============+=========+============+
| **Pune**      | 3.91         | 3.98         | **      | ▲ Delivery |
|               |              |              | +0.07** | \> Dining  |
+---------------+--------------+--------------+---------+------------+

  ----------------------------------------------------------------------------
  **New Delhi**   3.88           3.95           **+0.07**   ▲ Delivery   
                                                            \> Dining    
  --------------- -------------- -------------- ----------- ------------ -----
  **Hyderabad**   3.86           3.94           **+0.08**   ▲ Delivery   
                                                            \> Dining    

  **Mumbai**      3.83           3.91           **+0.08**   ▲ Delivery   
                                                            \> Dining    

  **Raipur**      3.95           4.01           **+0.06**   ▲ Delivery   
                                                            \> Dining    

  **Goa**         3.82           3.76           **-0.06**   ▼ Dining \>  
                                                            Delivery     

  **Bangalore**   3.70           3.79           **+0.09**   ▲ Delivery   
                                                            \> Dining    
  ----------------------------------------------------------------------------

#  ​City-Cuisine Rating Gap Heatmap 

> The highlight table cross-references 8 cuisine types against all 13
> cities, with colour encoding representing the rating gap magnitude.
> Sichuan cuisine shows the largest gaps across multiple cities --- a
> high-risk, high- volatility category. Pizza and Fast Food exhibit
> relatively stable, moderate gaps --- safer bets for consistent rating
> performance. Beverages and Shakes show minimal gaps, consistent with
> their lower complexity of execution.

+---------+------+------+------+------+------+------+------+------+
| > **    | *    | **   | *    | **Pu | *    | **C  | **G  | **   |
| Cuisine | *Ban | Mumb | *Del | ne** | *Hyd | henn | oa** | Raip |
| > \\    | galo | ai** | hi** |      | erab | ai** |      | ur** |
| >       | re** |      |      |      | ad** |      |      |      |
|  City** |      |      |      |      |      |      |      |      |
+=========+======+======+======+======+======+======+======+======+
| **Bi    | -0.1 | +0.2 | -0.1 | -0.0 | -0.1 | +0.2 | +0.3 | -0.0 |
| ryani** |      |      |      |      |      |      |      |      |
+---------+------+------+------+------+------+------+------+------+
| **      | -0.1 | -0.1 | -0.1 | -0.1 | -0.1 | -0.0 | -0.1 | -0.1 |
| Pizza** |      |      |      |      |      |      |      |      |
+---------+------+------+------+------+------+------+------+------+
| **Ch    | +0.2 | +0.3 | +0.1 | -0.1 | +0.2 | +0.3 | +0.3 | -0.1 |
| inese** |      |      |      |      |      |      |      |      |
+---------+------+------+------+------+------+------+------+------+
| **Si    | +0.4 | +0.3 | +0.4 | +0.2 | +0.4 | +0.3 | -0.1 | +0.2 |
| chuan** |      |      |      |      |      |      |      |      |
+---------+------+------+------+------+------+------+------+------+
| **Fast  | -0.1 | -0.1 | -0.0 | -0.1 | -0.1 | -0.1 | -0.1 | -0.0 |
| Food**  |      |      |      |      |      |      |      |      |
+---------+------+------+------+------+------+------+------+------+
| **Beve  | -0.0 | -0.0 | -0.0 | -0.0 | -0.0 | -0.0 | -0.0 | -0.0 |
| rages** |      |      |      |      |      |      |      |      |
+---------+------+------+------+------+------+------+------+------+
| **S     | -0.0 | -0.1 | -0.0 | -0.0 | -0.1 | -0.0 | -0.1 | -0.0 |
| hakes** |      |      |      |      |      |      |      |      |
+---------+------+------+------+------+------+------+------+------+
| **Des   | -0.1 | +0.2 | -0.1 | -0.0 | +0.2 | +0.1 | +0.3 | -0.1 |
| serts** |      |      |      |      |      |      |      |      |
+---------+------+------+------+------+------+------+------+------+

> *Legend: Deep green = low/negative gap (dining ≥ delivery) \| Orange =
> moderate gap \| Red = high gap (delivery \>\> dining)*
>
> Three statistical tests were conducted to validate the EDA findings
> and ensure that observed patterns reflect genuine signal rather than
> sampling noise.

#  ​Paired T-Test: Dining Rating vs. Delivery Rating 

> A paired-samples T-test was conducted to determine whether the
> observed difference between average dining ratings (3.827) and average
> delivery ratings (3.959) was statistically significant. The test
> returned a p-value below 0.001, decisively rejecting the null
> hypothesis of equal means. This confirms that the -0.1321 rating gap
> is a reproducible, systemic pattern --- not a sampling artefact.

#  ​ANOVA: Rating Variance Across Cities 

> A one-way ANOVA was applied to test whether average dining ratings
> differ significantly across the 13 cities. The significant result (p
> \< 0.05) confirms that city is a meaningful predictor of dining rating
> --- justifying city- segmented strategy rather than a
> one-size-fits-all approach. Post-hoc analysis identifies Raipur and
> Pune as highest-performing markets and Bangalore and Ahmedabad as
> lowest.

#  ​Correlation Analysis: Price vs. Rating 

> Pearson correlation between item price and dining rating returned a
> weak positive correlation (r ≈ 0.18), indicating that higher price is
> a modest predictor of higher ratings but explains less than 4% of
> rating variance. This has a critical business implication: premium
> pricing does not guarantee premium experience perception.

+-----------+--------------+--------------+--------+------------------+
| **Test**  | > **Groups   | > **Key      | >      | > **Conclusion** |
|           | > Compared** | >            |  **p-v |                  |
|           |              |  Statistic** | alue** |                  |
+===========+==============+==============+========+==================+
| Paired    | Dining vs    | Mean diff. = | \<     | Significant ---  |
| T-Test    | Delivery     | −0.132       | 0.001  | delivery         |
|           | Rating       |              |        | consistently     |
|           |              |              |        | higher           |
+-----------+--------------+--------------+--------+------------------+
| One-Way   | Rating       | F-statistic  | \<     | City is a        |
| ANOVA     | across 13    | significant  | 0.05   | significant      |
|           | Cities       |              |        | predictor of     |
|           |              |              |        | rating           |
+-----------+--------------+--------------+--------+------------------+
| Pearson   | Price vs     | r ≈ 0.18     | \<     | Price ≠ quality  |
| Corr.     | Dining       | (weak        | 0.05   | guarantee        |
|           | Rating       | positive)    |        |                  |
+-----------+--------------+--------------+--------+------------------+

> Two Tableau dashboards were built to serve different analytical
> audiences --- the first targeting operational managers who need a
> city-level overview, and the second targeting category strategists who
> need deep-dive rating gap intelligence.

+---------------+--------------------+---------+---------------------+
| >             | > **Charts         | > **Aud | > **Primary         |
| **Dashboard** | > Included**       | ience** | > Question**        |
+===============+====================+=========+=====================+
| Dashboard 1   | KPI tiles + Avg    | Ope     | > Which cities have |
| --- Zomato    | Dining Rating bar  | rations | > highest/lowest    |
| Metro         | chart + City map   |         | > dining ratings?   |
| Analytics     |                    |         |                     |
+---------------+--------------------+---------+---------------------+
| Dashboard 2   | KPI tiles +        | S       | > Where is the      |
| --- Zomato    | City-Cuisine       | trategy | > rating gap        |
| Rating        | heatmap + Scatter  |         | > largest, and      |
| Analytics     | plot + Histogram   |         | > which cuisines    |
|               |                    |         | > are most at risk? |
+---------------+--------------------+---------+---------------------+
| Dashboard 3   | Avg Item Price by  | Pricing | > Which cuisines    |
| --- Menu      | Cuisine + Price    |         | > and cities show   |
| Price         | Tier Distribution  |         | > pricing           |
| Analytics     | by City            |         | > anomalies?        |
+---------------+--------------------+---------+---------------------+

> Dashboard 1 features an interactive City filter that allows users to
> isolate individual metro markets across all charts simultaneously.
> Dashboard 2 adds a Cuisine filter enabling drill-down to specific food
> categories. Both dashboards use a consistent dark theme with Zomato
> red as the primary accent color, ensuring visual brand coherence with
> the subject matter.

#  Price Intelligence --- Avg Item Price by Cuisine  {#price-intelligence-avg-item-price-by-cuisine .unnumbered}

> **Average Item Price by Cuisine (₹)**
>
> ██████████████████████████████
>
> ███████████████████████
>
> ██████████████████████
>
> ███████████████████
>
> █████████████████
>
> ████████████████
>
> ███████████████
>
> ███████████████
>
> ████████████
>
> ███████████

+------------+---------------------------------------------------------+
|            | > **Action:** Identify the bottom 20% of restaurants by |
|            | > dining rating within each city and                    |
+============+=========================================================+
|            | > mandate a service audit covering wait times, staff    |
|            | > training, and ambience scoring. Set                   |
+------------+---------------------------------------------------------+
| **Rec.     | > a minimum dining rating floor of 3.7 before allowing  |
| 01**       | > premium price tier listing on the platform.           |
|            |                                                         |
| *          |                                                         |
| *Dine-In** |                                                         |
+------------+---------------------------------------------------------+
| > **Ex     |                                                         |
| perience** |                                                         |
| >          |                                                         |
| > **P      |                                                         |
| rogramme** |                                                         |
+------------+---------------------------------------------------------+
|            | > **Est. Impact:** A 0.1-point average improvement in   |
|            | > dining ratings across 826                             |
+------------+---------------------------------------------------------+
|            | > restaurants would close the dining-delivery gap by    |
|            | > approximately 75%, reducing                           |
+------------+---------------------------------------------------------+
|            | > churn from in-person customers who leave without      |
|            | > re-ordering.                                          |
+------------+---------------------------------------------------------+

+------------+---------------------------------------------------------+
|            | > **Action:** Publish city-level pricing benchmarks     |
|            | > derived from the Avg Item Price                       |
+============+=========================================================+
|            | > analysis, segmented by cuisine and price tier.        |
|            | > Restaurants pricing more than 25%                     |
+------------+---------------------------------------------------------+
| > **Rec.   | > above city-cuisine median without a corresponding     |
| > 02**     | > rating premium should receive automated pricing       |
| >          | > review alerts.                                        |
| > **City-  |                                                         |
| Specific** |                                                         |
+------------+---------------------------------------------------------+
| >          |                                                         |
|  **Pricing |                                                         |
| > Gu       |                                                         |
| idelines** |                                                         |
+------------+---------------------------------------------------------+
|            | > **Est. Impact:** Correcting price-rating misalignment |
|            | > in Goa and Ahmedabad is                               |
+------------+---------------------------------------------------------+
|            | > projected to improve repeat order rates by 10-15% as  |
|            | > customer perceived value                              |
+------------+---------------------------------------------------------+
|            | > improves.                                             |
+------------+---------------------------------------------------------+

+------------+---------------------------------------------------------+
|            | > **Action:** Classify cuisines into Low Risk           |
|            | > (Beverages, Shakes, Fast Food), Medium                |
+============+=========================================================+
|            | > Risk (Chinese, Biryani, Pizza), and High Risk         |
|            | > (Sichuan, Desserts in specific cities)                |
+------------+---------------------------------------------------------+
| > **Rec.   | > based on rating gap volatility. New restaurant        |
| > 03**     | > onboarding should present this risk classification to |
| >          | > help operators make data-informed cuisine selection   |
| >          | > decisions.                                            |
|  **Cuisine |                                                         |
| > Risk**   |                                                         |
+------------+---------------------------------------------------------+
| **Classi   |                                                         |
| fication** |                                                         |
|            |                                                         |
| **System** |                                                         |
+------------+---------------------------------------------------------+
|            | > **Est. Impact:** Steering 10% of new restaurant       |
|            | > sign-ups from High Risk to Low/Medium                 |
+------------+---------------------------------------------------------+
|            | > Risk cuisines in their first year is projected to     |
|            | > reduce early-stage negative rating                    |
+------------+---------------------------------------------------------+
|            | > events and improve new restaurant retention.          |
+------------+---------------------------------------------------------+

+------------+---------------------------------------------------------+
|            | > **Action:** Allocate incremental marketing and        |
|            | > restaurant acquisition budget toward                  |
+============+=========================================================+
|            | > Raipur-tier metros (smaller, high-rating cities) over |
|            | > saturated markets like Bangalore.                     |
+------------+---------------------------------------------------------+
| **Rec.     | > These markets demonstrate that lower restaurant       |
| 04**       | > density correlates with higher average ratings.       |
|            |                                                         |
| **         |                                                         |
| Prioritise |                                                         |
| Market**   |                                                         |
+------------+---------------------------------------------------------+
| > **D      |                                                         |
| evelopment |                                                         |
| > in**     |                                                         |
| >          |                                                         |
| > **R      |                                                         |
| aipur-Tier |                                                         |
| > Cities** |                                                         |
+------------+---------------------------------------------------------+
|            | > **Est. Impact:** A 20% increase in restaurant count   |
|            | > in high-rating smaller cities, if                     |
+------------+---------------------------------------------------------+
|            | > quality-vetted, could sustain or improve city average |
|            | > ratings while expanding GMV at                        |
+------------+---------------------------------------------------------+
|            | > lower customer acquisition cost than in saturated     |
|            | > metros.                                               |
+------------+---------------------------------------------------------+

#  Quantified Impact Summary  {#quantified-impact-summary .unnumbered}

+--------------------+---------------+--------------------------------+
| >                  | **Lever**     | > **Projected Outcome**        |
| **Recommendation** |               |                                |
+====================+===============+================================+
| Dine-In Experience | +0.1 dining   | \~75% closure of               |
| Programme          | rating        | dining-delivery gap; reduced   |
|                    |               | dine-in churn                  |
+--------------------+---------------+--------------------------------+
| City Pricing       | Price-rating  | 10-15% improvement in repeat   |
| Guidelines         | alignment     | order rates in affected cities |
+--------------------+---------------+--------------------------------+
| Cuisine Risk       | 10% shift to  | Reduction in early-stage       |
| Classification     | lower-risk    | negative ratings for new       |
|                    | cuisines      | restaurants                    |
+--------------------+---------------+--------------------------------+
| Raipur-Tier Market | +20%          | Sustained high city ratings;   |
| Development        | restaurant    | lower CAC vs. saturated metros |
|                    | count         |                                |
+--------------------+---------------+--------------------------------+

> **[Limitations]{.underline}**
>
> Three constraints bound the current analysis. First, the
> 826-restaurant sample, while sufficient for statistically significant
> city-level findings, is too small for cuisine-level subgroup analysis
> with high confidence, particularly for niche categories like Sichuan.
> Second, the absence of time-series order data means seasonal patterns
> and trend analysis are not currently possible. Third, the dataset
> represents a snapshot rather than a live feed
>
> --- findings are valid for the period covered but may shift as
> Zomato\'s restaurant mix evolves.

#  Future Scope  {#future-scope .unnumbered}

> Phase 2 of ShopLens should pursue three parallel workstreams. First,
> dataset expansion to include order volume and revenue data ---
> achievable through Zomato\'s public API or expanded Kaggle datasets
> --- would allow the team to move from rating-based analysis to
> GMV-based analysis. Second, integration of time-series data would
> unlock seasonal trend analysis and demand forecasting for cuisine
> categories by city. Third, a real-time Tableau integration with a live
> data feed would convert the current retrospective dashboard into a
> prospective monitoring tool --- alerting restaurant managers to
> emerging rating gaps before they compound into sustained brand damage.

+---------------+-----------+---------------+------------------------+
| > **Team      | **Role**  | > **Primary   | > **Deliverables**     |
| > Member**    |           | > Respo       |                        |
|               |           | nsibilities** |                        |
+===============+===========+===============+========================+
| **Phalak      | St        | End-to-end    | > EDA chart library,   |
| Sharma**      | atistical | project       | > Report made, Dataset |
|               | Analyst   | scoping,      | > finding & cleaning   |
|               |           | timeline      |                        |
|               |           | management,   |                        |
|               |           | final         |                        |
|               |           | integration   |                        |
|               |           | of all        |                        |
|               |           | workstreams   |                        |
+---------------+-----------+---------------+------------------------+
| **Harshit     | Data      | ETL pipeline  | > ETL Python scripts,  |
| Kudhial**     | Engineer  | design and    | > Dashboard 3          |
|               |           | execution,    |                        |
|               |           | data sourcing |                        |
|               |           | and           |                        |
|               |           | preprocessing |                        |
+---------------+-----------+---------------+------------------------+
| **Shiva       | Project   | Hypothesis    | > T-Test & ANOVA       |
| Sharma**      | Lead      | test design,  | > outputs, KPI summary |
|               |           | KPI           | > sheet, Dashboard 2   |
|               |           | computation,  | > (Tableau), PPT       |
|               |           | statistical   |                        |
|               |           | i             |                        |
|               |           | nterpretation |                        |
+---------------+-----------+---------------+------------------------+
| **Pratyush    | Visu      | Tableau       | > Final project report |
| Parida**      | alization | dashboard     | > document, references |
|               | S         | design, chart | > list                 |
|               | pecialist | type          |                        |
|               |           | selection,    |                        |
|               |           | colour        |                        |
|               |           | encoding      |                        |
+---------------+-----------+---------------+------------------------+
| **Piyush      | Research  | Dataset       | **Data Sourcing, ETL   |
| Raj**         | & QA      | validation,   | pipeline               |
|               |           | insight       | (Python/Pandas);       |
|               |           | review,       | tc;lean_lab_master\_** |
|               |           | r             |                        |
|               |           | ecommendation | **v3.csv; GitHub,**    |
|               |           | research      | ta                     |
|               |           |               | bleau_ready_zomato.csv |
|               |           |               |                        |
|               |           |               | **repository           |
|               |           |               | structure.**           |
+---------------+-----------+---------------+------------------------+
| **S. Shiva    | Docu      | Report        | > T-Test & ANOVA       |
| Sankar M.     | mentation | writing,      | > outputs, KPI summary |
| K.**          | Lead      | section       | > sheet, Dashboard 1   |
|               |           | drafting,     | > (Tableau), PPT       |
|               |           | reference     |                        |
|               |           | compilation   |                        |
+---------------+-----------+---------------+------------------------+

+-----------------+----------------------------------------------------+
| > **GitHub      | > SectionD_G6_ZomatoMetroAnalytics                 |
| > Repository**  |                                                    |
+=================+====================================================+
| > **Dataset     | > kaggle.com/datas                                 |
| > Source**      | ets/narsingraogoud/zomato-restaurants-dataset-for- |
|                 | > metropolitan-areas                               |
+-----------------+----------------------------------------------------+

> ■■■■■■■■■■■■■■■■■■■■■■■■■
>
> *Newton School of Technology \| Team G-6 (Section D) \| April 2026*
