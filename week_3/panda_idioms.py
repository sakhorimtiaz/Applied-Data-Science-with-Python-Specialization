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


df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv")
def min_max_1(row):
    data=row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    result=pd.Series({"min":np.min(data),"max":np.max(data)})
    return result

p=df.apply(min_max_1, axis="columns").head()
print(p)

df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv")
def min_max(row):
    data=row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row["min"]=np.min(data)
    row["max"]=np.max(data)
    return row

p=df.apply(min_max, axis="columns").head()
print(p)

#with lambda
p=df.apply(min_max, axis="columns").head()
#print(p)
rows = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013','POPESTIMATE2014',
        'POPESTIMATE2015']
print(df.apply(lambda x:np.max(x[rows]),axis="columns").head())

#another example
def get_state_region(x):
    northeast = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire',
                 'Rhode Island','Vermont','New York','New Jersey','Pennsylvania']
    midwest = ['Illinois','Indiana','Michigan','Ohio','Wisconsin','Iowa',
               'Kansas','Minnesota','Missouri','Nebraska','North Dakota',
               'South Dakota']
    south = ['Delaware','Florida','Georgia','Maryland','North Carolina',
             'South Carolina','Virginia','District of Columbia','West Virginia',
             'Alabama','Kentucky','Mississippi','Tennessee','Arkansas',
             'Louisiana','Oklahoma','Texas']
    west = ['Arizona','Colorado','Idaho','Montana','Nevada','New Mexico','Utah',
            'Wyoming','Alaska','California','Hawaii','Oregon','Washington']

    if x in northeast:
        return "Northeast"
    if x in midwest:
        return "Midwest"
    if x in south:
        return "South"
    else:
        return "West"

df["state_region"]=df["STNAME"].apply(lambda x:get_state_region(x))
print(df[["STNAME","state_region"]].head())
