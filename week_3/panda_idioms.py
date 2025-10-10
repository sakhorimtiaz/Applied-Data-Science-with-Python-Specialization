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
    return readable

def conventional():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv")

    new_df=df[df["SUMLEV"]==50]
    new_df.set_index(["STNAME", "CTYNAME"],inplace=True)
    new_df.rename(columns={"ESTIMATESBASE2010": "Estimates Base 2010"})
    return new_df

t1=timeit.timeit(pandorable,number=10)
t2=timeit.timeit(conventional,number=10)
print(t1)
print(t2)
