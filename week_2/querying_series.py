def loc_and_iloc():
    students_classes = {'Alice': 'Physics',
                        'Jack': 'Chemistry',
                        'Molly': 'English',
                        'Sam': 'History'}
    s = pd.Series(students_classes)
    print(s.iloc[3])
    print((s.loc["Molly"]))

def finding_sum_slow(grades):
    #grades = pd.Series([90, 80, 70, 60])
    total=0
    for grade in grades:
        total+=grade
    return total/len(grades)
def finding_sum_fast(grades):
    #grades = pd.Series([90, 80, 70, 60])
    total=np.sum(grades)
    return total/len(grades)

import timeit
def vectorization():
    numbers=pd.Series(np.random.randint(0,1000,10000))
    print(numbers.head())
    print(len(numbers))
    print(timeit.timeit(lambda : finding_sum_slow,number=100))
    print(timeit.timeit(lambda : finding_sum_fast, number=100))

def increase():
    numbers = pd.Series(np.random.randint(0, 1000, 10000))
    print(numbers.head())
    numbers += 2
    print(numbers.head())

def merging():
    students_classes = pd.Series({'Alice': 'Physics',
                                  'Jack': 'Chemistry',
                                  'Molly': 'English',
                                  'Sam': 'History'})
    kelly_classes = pd.Series(['Philosophy', 'Arts', 'Math'], index=['Kelly', 'Kelly', 'Kelly'])
    all_students_classes=pd.concat([students_classes,kelly_classes])
    print(all_students_classes)
    print(students_classes)
    print(all_students_classes.loc["Kelly"])
