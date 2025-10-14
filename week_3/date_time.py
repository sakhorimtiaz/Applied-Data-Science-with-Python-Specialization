import pandas as pd
import numpy as np

#print(pd.Timestamp("14/10/2025 9:2m"))
#print(pd.Timestamp(year=2025,month=10,day=14,hour=9,minute=10,second=35))
#print(pd.Timestamp(year=2025,month=10,day=14,hour=9,minute=10,second=35).isoweekday())
#print(pd.Timestamp(year=2025,month=10,day=14,hour=9,minute=10,second=35).month)

#print(pd.Period("10/2005"))
#print(pd.Period("10/2005")+2)
#print(pd.Period("10/14/2005")+2)
#print(pd.Period("14/10/2025 9:2am")-2)
def date_time_index_period_index():
    t1 = pd.Series(data=list("abc"),
                   index=[pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
    print(t1)
    print(t1.index)
    t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'),
                                 pd.Period('2016-11')])
    print(t2)
    print(t2.index)
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']

# And just some random data
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1,
                   columns=list('ab'))

print(pd.to_datetime("4.7.12",dayfirst=True))

def time_delta():
    t4=pd.Timestamp("9/3/2025")-pd.Timestamp("9/1/2025")
    print(t4)
    t5=pd.Timestamp("9/3/2025")+pd.Timedelta("12D 3H")
    print(t5)

def offsets():
    t6 = pd.Timestamp("9/3/2025").weekday()
    print(t6)
    t7 = pd.Timestamp("9/3/2025") + pd.offsets.Week()
    print(t7)
    t8 = pd.Timestamp("9/3/2025") + pd.offsets.MonthEnd()
    print(t8)
    t9 = pd.Timestamp("9/3/2025") + pd.offsets.MonthBegin()
    print(t9)
    t10 = pd.Timestamp("10/17/2025") + pd.offsets.BusinessDay()
    print(t10)
def working_with_dates():
    dates1=pd.date_range("10/1/2016",periods=9,freq="2W-SUN")
    #print(dates1)
    dates2=pd.date_range("10/1/2016",periods=9,freq="B")
    #print(dates2)
    dates3 = pd.date_range("10/1/2016", periods=9, freq="QS-JUN")
    #print(dates3)
