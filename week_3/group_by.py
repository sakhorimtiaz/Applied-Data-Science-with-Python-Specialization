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

df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv")
df=df.set_index("STNAME")

def set_batch_number(item):
    if item[0]<"M":
        return 0
    if item[0]<"Q":
        return 1
    else:
        return 2

for group, frame in df.groupby(set_batch_number):
    print(f'There are {len(frame)} records in group  {group}  for processing.')
def grouping_fun(item):
    # Check the "review_scores_value" portion of the index. item is in the format of
    # (cancellation_policy,review_scores_value
    if item[1] == 10.0:
        return (item[0],"10.0")
    else:
        return (item[0],"not 10.0")

for group, frame in df.groupby(grouping_fun):
    print(group)

def aggregation():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\listings.csv")
    df = df.reset_index()
    # df=df.groupby("cancellation_policy").agg({"review_scores_value":np.nanmean})
    df = df.groupby("cancellation_policy").agg(
        {"review_scores_value": (np.nanmean, np.nanstd), "reviews_per_month": np.nanmean})
    print(df.head())

def transformtion_and_filtering():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\listings.csv")
    cols = ["cancellation_policy", "review_scores_value"]
    transform_df = df[cols].groupby("cancellation_policy").transform(np.nanmean)
    print(transform_df.head())
    transform_df.rename({'review_scores_value': 'mean_review_scores'}, axis='columns', inplace=True)
    df = df.merge(transform_df, left_index=True, right_index=True)
    print(df.head())
    df['mean_diff'] = np.absolute(df['review_scores_value'] - df['mean_review_scores'])
    print(df['mean_diff'].head())
    df.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['review_scores_value']) > 9.2)
