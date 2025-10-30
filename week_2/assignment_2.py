
#Question-1
import pandas as pd
import numpy as np

def proportion_of_education():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\NISPUF17.csv")

    counts = df['EDUC1'].value_counts()
    print(counts)
    total = counts.sum()

    proportion = counts / total
    print(proportion)

    result = {"less than high school": proportion[1], "high school": proportion[2],
              "more than high school but not college": proportion[3], "college": proportion[4]}
    return result

#Question-2
def average_influenza_doses():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\NISPUF17.csv")
    df=df[["CBF_01", "P_NUMFLU"]]
    df=df.dropna()
    #print(df.head())

    breastfed=df[df["CBF_01"]==1]
    not_breastfed = df[df["CBF_01"] == 2]
    #print(breastfed)
    #print(not_breastfed)

    avg_breastfed=breastfed["P_NUMFLU"].mean()
    avg_not_breastfed = not_breastfed["P_NUMFLU"].mean()
    #print(avg_breastfed)
    #print(avg_not_breastfed)
    return (avg_breastfed,avg_not_breastfed)

#Question-3
def chickenpox_by_sex():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\NISPUF17.csv")
    df=df[["SEX", "HAD_CPOX", "P_NUMVRC"]]
    #print(df.head())

    df=df[df["P_NUMVRC"]>=1]
    df=df[df["HAD_CPOX"].isin([1,2])]
    #print(df.head())

    result={}
    sex_map={1:"male",2:"female"}
    for sex,label in sex_map.items():
        group_df=df[df["SEX"]==sex]
        had_chickenpox=group_df[group_df["HAD_CPOX"]==1]
        not_had_chickenpox = group_df[group_df["HAD_CPOX"] == 2]
        #print(had_chickenpox)
        #print(not_had_chickenpox)

        had=len(had_chickenpox)
        not_had=len(not_had_chickenpox)
        ratio=had/not_had
        result[label]=ratio
    return result

#Question-4
def corr_chickenpox():
    import pandas as pd
    import numpy as np
    from scipy import stats as sat

    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\NISPUF17.csv")

    df = df[["HAD_CPOX", "P_NUMVRC"]]

    df = df.dropna()

    df = df[df["HAD_CPOX"].isin([1, 2])]

    corr, pval = sat.pearsonr(df["HAD_CPOX"], df["P_NUMVRC"])

    print("Correlation:", corr)
    print("p-value:", pval)

    return corr
