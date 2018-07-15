import  pandas as pd
import random

dataframe=pd.DataFrame(random.randint(1,101),['A','B','C','D','E'],['W','X','Y','Z'])
print(dataframe)
print(dataframe['W'])
#print(type(dataframe['W']))
