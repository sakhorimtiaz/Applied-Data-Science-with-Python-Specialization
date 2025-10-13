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
    my_categories = pd.CategoricalDtype(categories=["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D"],
                                        ordered=True)
    grades = df["Grades"].astype(my_categories)
    df = df[df["Grades"] > "C"]
    print(grades.head())
