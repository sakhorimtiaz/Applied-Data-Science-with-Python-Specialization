import pandas as pd
import numpy as np
from scipy import stats as sat
df=pd.read_csv ('datasets/grades.csv')
#print(df.head())
print(f"there are {df.shape[0]} rows and {df.shape[1]} columns")

def assignment():
    early_finishers = df[pd.to_datetime(df["assignment1_submission"]) < "2016"]
    # print(early_finishers.head())
    late_finishers = df[~df.index.isin(early_finishers.index)]
    # print(late_finishers.head())
    print(early_finishers['assignment1_grade'].mean(), late_finishers['assignment1_grade'].mean())
    print(early_finishers['assignment2_grade'].mean(), late_finishers['assignment2_grade'].mean())
    print(early_finishers['assignment3_grade'].mean(), late_finishers['assignment3_grade'].mean())
    print(early_finishers['assignment4_grade'].mean(), late_finishers['assignment4_grade'].mean())
    print(early_finishers['assignment5_grade'].mean(), late_finishers['assignment5_grade'].mean())
    print(early_finishers['assignment6_grade'].mean(), late_finishers['assignment6_grade'].mean())

    a = sat.ttest_ind(early_finishers['assignment1_grade'], late_finishers['assignment1_grade'])
    b = sat.ttest_ind(early_finishers['assignment2_grade'], late_finishers['assignment2_grade'])
    c = sat.ttest_ind(early_finishers['assignment3_grade'], late_finishers['assignment3_grade'])
    d = sat.ttest_ind(early_finishers['assignment4_grade'], late_finishers['assignment4_grade'])
    e = sat.ttest_ind(early_finishers['assignment5_grade'], late_finishers['assignment5_grade'])
    f = sat.ttest_ind(early_finishers['assignment6_grade'], late_finishers['assignment6_grade'])
    print(a, b, c, d, e, f)

df1=pd.DataFrame([np.random.random(100) for x in range(100)])
#print(df1)
df2=pd.DataFrame([np.random.random(100) for x in range(100)])
#print(df2)
def test_columns(alpha=0.1):
    num_diff=0
    for col in df1.columns:
        teststat,pval=sat.ttest_ind(df1[col],df2[col])
        if pval<=alpha:
            print(f"Column {col} is statistically significantly different at alpha={alpha}, pval={pval}")
            num_diff+=1
    percentage=num_diff/len(df1.columns)
    print(f"Total number different was {num_diff}, which is {percentage}%")
#test_columns(alpha=0.1)
df2=pd.DataFrame([np.random.chisquare(df=1,size=100) for x in range(100)])
test_columns(alpha=0.1)
