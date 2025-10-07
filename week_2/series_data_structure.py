import pandas as pd
def pandas_series():
    students = ['Alice', 'Jack', 'Molly']
    student = ['Alice', 'Jack', None]
    numbers = [1, 2, 3]
    number = [1, 2, None]
    print(pd.Series(students))
    print(pd.Series(numbers))
    print(pd.Series(student))
    print(pd.Series(number))

import numpy as np
def checking_nan_and_none():
    print(np.nan == np.nan)
    print(np.nan == None)
    print(np.isnan(np.nan))
def dictionary_and_tuples():
    students_scores = {'Alice': 'Physics',
                       'Jack': 'Chemistry',
                       'Molly': 'English'}
    print(pd.Series(students_scores))
    students = [("Alice", "Brown"), ("Jack", "White"), ("Molly", "Green")]
    print(pd.Series(students))
    s = pd.Series(["Physics", "Chemistry", "English"], index=["Alice", "Jack", "Molly"])
    print(s)
    p = pd.Series(students_scores, index=["Alice", "Molly", "Sam"])
    print(p)
