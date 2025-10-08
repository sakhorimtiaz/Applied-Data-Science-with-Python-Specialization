def creating_dataframe_1():
    record1 = pd.Series({'Name': 'Alice',
                         'Class': 'Physics',
                         'Score': 85})
    record2 = pd.Series({'Name': 'Jack',
                         'Class': 'Chemistry',
                         'Score': 82})
    record3 = pd.Series({'Name': 'Helen',
                         'Class': 'Biology',
                         'Score': 90})
    df = pd.DataFrame([record1, record2, record3], index=["school1", "school2", "school3"])
    print((df))
def creating_dataframe_2():
    students = [{'Name': 'Alice',
                 'Class': 'Physics',
                 'Score': 85},
                {'Name': 'Jack',
                 'Class': 'Chemistry',
                 'Score': 82},
                {'Name': 'Helen',
                 'Class': 'Biology',
                 'Score': 90}]
    df=pd.DataFrame(students,index=["school1","school2","school1"])
    print(df.head())
    print(df.loc["school2"])
    print(df.loc[["school2"]])
    print(df.loc["school1","Name"])
    print(df.loc["school1"]["Name"]) #don't use this, slow
    print(df.loc[:,["Name","Score"]])
    print(type(df["Name"]))
    
    print(df.T)
    print(df.T.loc["Name"])

    d=df.drop("school2")
    print(d)

    copy_df=df.copy()
    copy_df.drop(columns="Name",inplace=False,axis=1)
    print(df)

    del copy_df["Class"]
    print(copy_df)
    print(df)
    df["Percentage"]=[34,45,60]
    print(df)
