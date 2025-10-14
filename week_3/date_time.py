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
