import numpy as np
import pandas as pd
import math

#data = pd.read_excel('example_data.xls', 'Sheet1', index_col=0)
data = pd.read_csv('example_data.csv',sep='\t',index_col=0)

#print data
#print data.columns
#print data.index

print data.loc[1]


#Find maximum current fix end. Gives the end bounds for how many intervals we
#need.
#data.loc[1].max()[2]
#max = data.loc[1].max()[2]
#interval = np.arange(0, max+100, 100)
#print interval

#Better way is to get the start and end

#print data.loc[1]['CURRENT_FIX_INTEREST_AREAS']

start = data.loc[1]['CURRENT_FIX_START']
end = data.loc[1]['CURRENT_FIX_END']
x = end - start


#get the intervals

mainInt = np.array([])
for i, j in zip(start.values, end.values):
    start = math.floor(i/100)*100
    end = math.ceil(j/100)*100
    interval = np.arange(start, end, 100)
    mainInt = np.hstack((mainInt, interval))
print mainInt

#for i,j in xrange(start.values, end.values):
#    interval = np.arange(i, j, 100)
#    print interval

#print x
#start = np.array(start.values)
#end = np.array(end.values)
#print start.values
#y = np.arange(start,end,100)
#print y

data['CURRENT_FIX_INTEREST_AREAS']
data['CURRENT_FIX_START']
data['CURRENT_FIX_END']
data['CURRENT_FIX_DURATION']



#data = data.set_index(data.columns[0])
#print data.index
#print data.columns
#
#
#print data.index['1']
