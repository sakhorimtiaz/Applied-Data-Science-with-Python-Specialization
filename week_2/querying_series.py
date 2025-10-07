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
vectorization()
