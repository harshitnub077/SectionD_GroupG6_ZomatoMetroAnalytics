from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

def normalize_columns(df):
    # Fixes column names to snake_case — "Cuisine " trailing space breaks KPI-2 groupby
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    result = df.copy()
    result.columns = cleaned
    return result

def basic_clean(df):
    result = normalize_columns(df)

    # Step 2 — Bangalore was split into 4 locality names in raw scrape; unified here
    bangalore_localities = {"Banaswadi", "Ulsoor", "Magrath Road", "Malleshwaram"}
    result["city"] = result["city"].str.strip()
    result["city"] = result["city"].apply(
        lambda x: "Bangalore" if x in bangalore_localities else x
    )

    # Step 3 — Remove 22,127 scraping duplicates; keeps KPI-2 vote counts accurate
    result = result.drop_duplicates().reset_index(drop=True)

    # Cast numerics so imputation and clipping work correctly
    result["dining_rating"]   = pd.to_numeric(result["dining_rating"],   errors="coerce")
    result["delivery_rating"] = pd.to_numeric(result["delivery_rating"], errors="coerce")
    result["prices"]          = pd.to_numeric(result["prices"],          errors="coerce")
    result["votes"]           = pd.to_numeric(result["votes"],           errors="coerce").astype("Int64")
    result["dining_votes"]    = pd.to_numeric(result["dining_votes"],    errors="coerce").astype("Int64")
    result["delivery_votes"]  = pd.to_numeric(result["delivery_votes"],  errors="coerce").astype("Int64")

    for col in result.select_dtypes(include="object").columns:
        result[col] = result[col].str.strip()

    # Step 4 — 26% dining ratings null; filled by City+Cuisine median, fallback to City
    result["dining_rating"] = result.groupby(["city", "cuisine"])["dining_rating"].transform(
        lambda x: x.fillna(x.median())
    )
    result["dining_rating"] = result.groupby("city")["dining_rating"].transform(
        lambda x: x.fillna(x.median())
    )

    # Step 5 — 1% delivery ratings null; city median is enough
    result["delivery_rating"] = result.groupby("city")["delivery_rating"].transform(
        lambda x: x.fillna(x.median())
    )

    # Step 6 — NaN in best_seller means no tag assigned; "None" makes it a valid category
    result["best_seller"] = result["best_seller"].fillna("None")

    # Step 7 — Price outliers clipped to [5, 3000]; no rows dropped
    result["prices"] = result["prices"].clip(lower=5, upper=3000)

    return result

def add_kpi_columns(df):
    # KPI-1: rating_gap = dining_rating - delivery_rating per restaurant
    # Positive gap means dine-in is rated better than delivery in that city
    result = df.copy()
    result["rating_gap"] = result["dining_rating"] - result["delivery_rating"]

    # KPI-2: avg_item_votes = average votes per cuisine, computed at item level
    # Identifies which cuisines have highest customer engagement
    cuisine_avg = result.groupby("cuisine")["votes"].transform("mean")
    result["avg_item_votes"] = cuisine_avg

    return result
