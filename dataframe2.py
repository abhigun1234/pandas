import  pandas as pd
import random
from numpy.random import randn
dataframe=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(dataframe)
print(dataframe['W'])
print(type(dataframe['W']))

#lets talk about conditional selection

print(dataframe>0)
'''booldataf=dataframe>0
print(booldataf)
print(dataframe[booldataf])
print(dataframe['W']>0)'''
