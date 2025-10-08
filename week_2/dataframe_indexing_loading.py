def dataframe_indexing_loading():
    df = pd.read_csv(r"C:\users\thinkpad\Downloads\mpg_output.csv", encoding="utf-8")
    print(df.head())

    new_df1 = df.rename(columns={"text_length": "tl"})
    print(new_df1.head())

    columns = df.columns
    print(columns)

    new_df2 = df.rename(mapper=str.strip, axis="columns")
    print(new_df2.head())

    cols = list(df.columns)
    cols = [x.upper().strip() for x in cols]
    df.columns = cols
    print(df.head())

    print(cols)
