import csv
with open(r"C:\Users\THINKPAD\Downloads\mpg.csv") as csvfile:
    mpg=list(csv.DictReader(csvfile))
#print(mpg)

number_of_cylinders=set(d["cyl"] for d in mpg)
#print(number_of_cylinders)

res=[]
for c in number_of_cylinders:
    total = 0
    count = 0
    for d in mpg:
        if d["cyl"]==c:
            total += float(d["cty"])
            count += 1
    res.append((c,total/count))
#print(res)

import datetime as dt
import time as tm

#print(tm.time())

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
"""for items in cheapest:
    print(items)"""

divisible_by_2= list(filter(lambda x:x %2 ==0,range(0,100)))
print(divisible_by_2)

divisible_by_2_new=[x for x in range (0,100) if x%2==0]
print(divisible_by_2_new)

