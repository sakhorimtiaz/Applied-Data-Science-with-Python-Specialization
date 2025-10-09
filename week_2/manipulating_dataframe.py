# process1_not_a_good_option
df=pd.read_csv(r"C:\Users\THINKPAD\Downloads\presidents.csv",encoding="utf-8")
print(df.head())
df["First"]=df["President"]
print(df.head())
df["First"]=df["First"].replace("[ ].*","",regex=True)
print(df.head())
del(df["First"])
print(df.head())
