import pandas as pd
df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\Admission_Predict.csv", encoding="utf-8")
df.columns=[x.lower().strip() for x in df.columns]
def process():
    print(df.head())
    admit_mask = df["chance of admit"] > 0.7
    print(admit_mask)
    print(df.where(admit_mask).head())
    print(df.where(admit_mask).dropna().head())

def boolean_mask():
    df[df["chance of admit"] > 0.7].head()
    p = df[["gre score", "toefl score"]].head()
    print(p)

def multiple_boolean_mask():
    a = df[(df["chance of admit"] > 0.7) & (df["chance of admit"] < 0.8)]
    print(a)
    b = df[(df["chance of admit"].gt(0.7)) & (df["chance of admit"].lt(0.8))]
    print(b)
    c = df[df["chance of admit"].gt(0.7).lt(0.8)]
    print(c)
