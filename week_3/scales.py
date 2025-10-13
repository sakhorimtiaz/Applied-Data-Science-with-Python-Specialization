
import pandas as pd
def unordered_category():
    df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                      index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good',
                             'ok', 'ok', 'ok', 'poor', 'poor'], columns=["Grades"])
    print(df)
    print(df.dtypes)
    c = df["Grades"].astype("category")
    print(c)
    df = df[df["Grades"] > "C"]
    print(df)

def ordered_category():
    df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                      index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good',
                             'ok', 'ok', 'ok', 'poor', 'poor'], columns=["Grades"])
    my_categories = pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                                        ordered=True)
    grades = df["Grades"].astype(my_categories)
    df = df[df["Grades"] > "C"]
    print(grades.head())

def dummy_values():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Subject': ['Math', 'Science', 'Math', 'English']
    })
    print(df)
    dummy_df = pd.get_dummies(df, columns=['Subject'])
    print(dummy_df)
def bin():
    df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\census.csv")
    df = df[df["SUMLEV"] == 50]
    df = df.set_index("STNAME").groupby(level=0)['CENSUS2010POP'].agg(np.average)
    print(df.head())
    print(pd.cut(df, 10))
