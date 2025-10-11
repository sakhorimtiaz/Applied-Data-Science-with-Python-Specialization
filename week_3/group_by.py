import pandas as pd
import numpy as np
def without_group_by():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv")
    df = df[df["SUMLEV"] == 50]
    #df.head()

    for state in df["STNAME"].unique():
        avg = np.average(df.where(df["STNAME"] == state).dropna()['CENSUS2010POP'])
        #print(f"{state} has an average population of {avg}")

print(timeit.timeit(without_group_by,number=3))

def with_group_by():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv")
    df = df[df["SUMLEV"] == 50]
    #df.head()

    for group,frame in df.groupby("STNAME"):
        avg=np.average(frame['CENSUS2010POP'])
        #print(f"{group} has an average population of {avg}")
print(timeit.timeit(with_group_by,number=3))
