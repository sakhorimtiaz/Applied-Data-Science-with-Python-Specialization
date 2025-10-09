# process1_without_regex_important_for_small_data
import pandas as pd
df=pd.read_csv(r"C:\Users\THINKPAD\Downloads\presidents.csv",encoding="utf-8")
def split_name(row):
    row["First"]=row["President"].split(" ")[0]
    row["Last"]=row["President"].split(" ")[-1]
    return row
df=df.apply(split_name,axis="columns")
print(df.head())

# process2_without_regex_important_for_big_data
def excellent_for_big_data():
  df=pd.read_csv(r"C:\Users\THINKPAD\Downloads\presidents.csv",encoding="utf-8")
  pattern="(^[\w]*)(?:.* )([\w]*$)"
  df["President"].str.extract(pattern).head()
  pattern="(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)"
  names=df["President"].str.extract(pattern).head()
  print(names)
  df["First"]=names["First"]
  df["Last"]=names["Last"]
  df.head()

# process2_not_a_good_option
def bad_process():
  df=pd.read_csv(r"C:\Users\THINKPAD\Downloads\presidents.csv",encoding="utf-8")
  print(df.head())
  df["First"]=df["President"]
  print(df.head())
  df["First"]=df["First"].replace("[ ].*","",regex=True)
  print(df.head())
  del(df["First"])

def time_date():
  df["Born"]=df["Born"].str.extract("([\w]{3} [\w]{1,2}, [\w]{4})")
  df["Born"].head()
  df["Born"]=pd.to_datetime(df["Born"])
  df["Born"].head()
print(df.head())
