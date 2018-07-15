import  numpy as np
import pandas as pd
lebels =['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
data=pd.Series(data =  my_data)
print(data)
# change index
# now we are passing data as a list and index as lebel
updateddata=pd.Series(data=my_data,index=lebels)
print(updateddata)

## you can also write  like
updateddata=pd.Series(my_data,lebels)
print(updateddata)

## index as a string
series1=pd.Series([1,2,3,4],['usa','chaina','Germany','india'])
print(series1)