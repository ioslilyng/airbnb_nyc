import pandas as pd
import numpy as np

def create_dummy_df(df, cat_cols, dummy_na):
    for col in  cat_cols:
        try:
            # for each cat add dummy var, drop original column
            df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)
        except:
            continue
    return df
    
def find_missing(df):
    miss = df.isnull().sum().sort_values(ascending=False)
    percent_miss = ((df.isnull().sum() * 100) / df.isnull().count().sort_values(ascending=False))
    missing = pd.concat([miss, percent_miss], axis=1, keys=['Total Missing Instances', '% Missing'], sort=False).sort_values('Total Missing Instances', ascending=False)
    return missing               