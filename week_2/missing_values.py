import pandas as pd

def grading():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\class_grades.csv", encoding="utf-8")

    mask = df.isnull()

    print(mask.head())
    print(df.head())
    print(df.dropna().head())
    df.fillna(0, inplace=True)  # modifies the original
    df.fillna(0, inplace=False)
    print(df.head())
  def replace():
    df = pd.DataFrame({'A': [1, 1, 2, 3, 4],
                       'B': [3, 6, 3, 8, 9],
                       'C': ['a', 'b', 'c', 'd', 'e']})
    print(df.head())
    rp=df.replace(1,100)
    print(rp)
    rpp=df.replace([1,3],[100,300])
    print(rpp)

    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\log.csv", encoding="utf-8")
    df = df.replace(to_replace=".*.html$", value="webpage", regex=True)
    print(df.head())
