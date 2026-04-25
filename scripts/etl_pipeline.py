from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

def normalize_columns(df):
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

    bangalore_localities = {"Banaswadi", "Ulsoor", "Magrath Road", "Malleshwaram"}
    result["city"] = result["city"].str.strip()
    result["city"] = result["city"].apply(
        lambda x: "Bangalore" if x in bangalore_localities else x
    )

    result = result.drop_duplicates().reset_index(drop=True)

    result["dining_rating"]   = pd.to_numeric(result["dining_rating"],   errors="coerce")
    result["delivery_rating"] = pd.to_numeric(result["delivery_rating"], errors="coerce")
    result["prices"]          = pd.to_numeric(result["prices"],          errors="coerce")
    result["votes"]           = pd.to_numeric(result["votes"],           errors="coerce").astype("Int64")
    result["dining_votes"]    = pd.to_numeric(result["dining_votes"],    errors="coerce").astype("Int64")
    result["delivery_votes"]  = pd.to_numeric(result["delivery_votes"],  errors="coerce").astype("Int64")

    for col in result.select_dtypes(include="object").columns:
        result[col] = result[col].str.strip()

    result["dining_rating"] = result.groupby(["city", "cuisine"])["dining_rating"].transform(
        lambda x: x.fillna(x.median())
    )
    result["dining_rating"] = result.groupby("city")["dining_rating"].transform(
        lambda x: x.fillna(x.median())
    )
    result["delivery_rating"] = result.groupby("city")["delivery_rating"].transform(
        lambda x: x.fillna(x.median())
    )

    result["best_seller"] = result["best_seller"].fillna("None")
    result["prices"]      = result["prices"].clip(lower=5, upper=3000)

    return result

def add_kpi_columns(df):
    result = df.copy()
    result["rating_gap"] = result["dining_rating"] - result["delivery_rating"]
    return result
