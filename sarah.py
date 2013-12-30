import numpy as np
import pandas as pd

#data = pd.read_excel('example_data.xls', 0, index_col=None, na_values=['NA'])
data = pd.read_csv('example_data.csv',sep='\t')

print data
print data.columns
print data.index

data = data.set_index(data.columns[0])
print data.index
print data.columns


