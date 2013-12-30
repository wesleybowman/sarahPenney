import numpy as np
import pandas as pd

#data = pd.read_excel('example_data.xls', 0, index_col=None, na_values=['NA'])
data = pd.read_csv('example_data.csv',sep='\t',index_col=0)

print data
print data.columns
print data.index

print data.loc[1]
print data.loc[2]

#data = data.set_index(data.columns[0])
#print data.index
#print data.columns
#
#
#print data.index['1']
