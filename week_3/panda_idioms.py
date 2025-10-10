import pandas as pd
import numpy as np
import timeit

def pandorable():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv")
    # print(df.head())

    readable = (df.where(df["SUMLEV"] == 50)
                .dropna()
                .set_index(["STNAME", "CTYNAME"])
                .rename(columns={"ESTIMATESBASE2010": "Estimates Base 2010"}))
    print(readable)
