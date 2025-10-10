import pandas as pd
def union_intersect_1():
    staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                             {'Name': 'Sally', 'Role': 'Course liasion'},
                             {'Name': 'James', 'Role': 'Grader'}])
    staff_df = staff_df.set_index("Name")
    student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                               {'Name': 'Mike', 'School': 'Law'},
                               {'Name': 'Sally', 'School': 'Engineering'}])
    student_df = student_df.set_index("Name")

    print(staff_df.head())
    print(student_df.head())
    union = pd.merge(staff_df, student_df, how="outer", left_index=True, right_index=True)
    intersect = pd.merge(staff_df, student_df, how="inner", left_index=True, right_index=True)
    # print(union)
    # print(intersect)
    a = pd.merge(staff_df, student_df, how="left", left_index=True, right_index=True)
    b = pd.merge(staff_df, student_df, how="right", left_index=True, right_index=True)
    # print(a)
    # print(b)
    staff_df = staff_df.reset_index()
    student_df = student_df.reset_index()
    pd.merge(staff_df, student_df, how="right", on="Name")
