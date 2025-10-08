def changing_index_position():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\Admission_Predict.csv", encoding="utf-8", index_col=0)
    print(df.head())
    df["Serial No."] = df.index
    df = df.set_index("Research")
    print(df.head())
    df = df.reset_index()
    print(df.head())

def bigdata():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv", encoding="utf-8")
    print(df.head())
    print(df["SUMLEV"].unique())
    print(df["REGION"].unique())
    filtered = df[df["SUMLEV"] == 50]
    print(filtered.head())
    columns_to_keep = ['STNAME', 'CTYNAME']
    print(df[columns_to_keep].head())
    df = df.set_index(columns_to_keep)
    print(df)
