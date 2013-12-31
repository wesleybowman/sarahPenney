from __future__ import division
import numpy as np
import pandas as pd
import math
import re

def sorted(trial,interval,aoi):
    if aoi=='':
        for k,v in enumerate(interval):
                    try:
                        if interval[k]<interval[k+1]:
                            if interval[k]< i <interval[k+1]:
                                first = interval[k+1]-i
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,0,0])
                            elif interval[k]< j <interval[k+1]:
                                last = j-interval[k]
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,0,0])
                            else:
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,0,0])

                    except IndexError:
                        pass
    if aoi=='1':
        for k,v in enumerate(interval):
                    try:
                        if interval[k]<interval[k+1]:
                            if interval[k]< i <interval[k+1]:
                                first = interval[k+1]-i
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),first,0,0,0])
                            elif interval[k]< j <interval[k+1]:
                                last = j-interval[k]
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),last,0,0,0])
                            else:
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),100,0,0,0])

                    except IndexError:
                        pass
    if aoi=='2':
        for k,v in enumerate(interval):
                    try:
                        if interval[k]<interval[k+1]:
                            if interval[k]< i <interval[k+1]:
                                first = interval[k+1]-i
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,first,0,0])
                            elif interval[k]< j <interval[k+1]:
                                last = j-interval[k]
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,last,0,0])
                            else:
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,100,0,0])

                    except IndexError:
                        pass
    if aoi=='3':
        for k,v in enumerate(interval):
                    try:
                        if interval[k]<interval[k+1]:
                            if interval[k]< i <interval[k+1]:
                                first = interval[k+1]-i
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,first,0])
                            elif interval[k]< j <interval[k+1]:
                                last = j-interval[k]
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,last,0])
                            else:
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,100,0])

                    except IndexError:
                        pass
    if aoi=='4':
        for k,v in enumerate(interval):
                    try:
                        if interval[k]<interval[k+1]:
                            if interval[k]< i <interval[k+1]:
                                first = interval[k+1]-i
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,0,first])
                            elif interval[k]< j <interval[k+1]:
                                last = j-interval[k]
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,0,last])
                            else:
                                time.append([trial,'{0}-{1}'.format(interval[k],interval[k+1]),0,0,0,100])

                    except IndexError:
                        pass

    return time


#data = pd.read_excel('example_data.xls', 'Sheet1', index_col=0)
data = pd.read_csv('example_data.csv',sep='\t',index_col=0)

trials = data.index.unique()
#new = pd.DataFrame(columns=['Time','1','2','3','4'])
new = pd.DataFrame()
#newData = {}


for trial in trials:
    if trial!=0:
        #print trial
        start = data.loc[trial]['CURRENT_FIX_START']
        end = data.loc[trial]['CURRENT_FIX_END']

        areas = data.loc[trial]['CURRENT_FIX_INTEREST_AREAS']
        areas = areas.values
        aoi = []
        for i in areas:
            areanumbers = re.sub(r'[^\w]', '', i)
            aoi.append(areanumbers)

        count = 0
        #mainInt = np.array([])

        for i, j in zip(start.values, end.values):
            start = math.floor(i/100)*100
            end = math.ceil(j/100)*100
            interval = np.arange(start, end+1, 100)

            time = []
            time = sorted(trial,interval,aoi[count])
    #        for k,v in enumerate(interval):
    #            try:
    #                if interval[k]<interval[k+1]:
    #                    if interval[k]< i <interval[k+1]:
    #                        first = interval[k+1]-i
    #                        time.append(['{0}-{1}'.format(interval[k],interval[k+1]),first])
    #                    elif interval[k]< j <interval[k+1]:
    #                        last = j-interval[k]
    #                        time.append(['{0}-{1}'.format(interval[k],interval[k+1]),last])
    #                    else:
    #                        time.append(['{0}-{1}'.format(interval[k],interval[k+1]),100])
    #
    #            except IndexError:
    #                pass
            #print time
            time = pd.DataFrame(time)
            time = time.set_index(0)
            new = pd.concat([new,time])

            #print aoi[count]
            #print time
            #print interval
        #    print len(interval)-3
            #print interval[1]-i, j-interval[-2]
            #mainInt = np.hstack((mainInt, interval))
            count += 1

            #new.set_index(trial,time)
            #new[aoi[count]]=time[1]
            #new['Time']=time

#        time = []
#        for i,v in enumerate(mainInt):
#            try:
#                if mainInt[i]<mainInt[i+1]:
#                    #print '{0}-{1}'.format(mainInt[i],mainInt[i+1])
#                    time.append('{0}-{1}'.format(mainInt[i],mainInt[i+1]))
#            except IndexError:
#                pass


#print mainInt
new.columns=['Time','% in 1','% in 2','% in 3','% in 4']
print new
print new.index
print new.columns
print new.values

new.to_csv('test.csv')
    #print newData


'''
    mainInt = np.array([])
    for i, j in zip(start.values, end.values):
        start = math.floor(i/100)*100
        end = math.ceil(j/100)*100

        interval = np.arange(start, end, 100)
        #interval[1]-i, j-interval[-2]
        #print interval
        mainInt = np.hstack((mainInt, interval))
    #print mainInt
'''


'''

#print data
#print data.columns
#print data.index

#print data.loc[1]


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
#x = end - start


#get the intervals
areas = data.loc[1]['CURRENT_FIX_INTEREST_AREAS']
aoi = []
for i in areas.values:
    areanumbers = re.sub(r'[^\w]', '', i)
    aoi.append(areanumbers)
    #print aoi=='1'
    #print type(aoi)

print aoi
count = 0
mainInt = np.array([])

for i, j in zip(start.values, end.values):
    start = math.floor(i/100)*100
    end = math.ceil(j/100)*100
    interval = np.arange(start, end+1, 100)

    time = []
    for k,v in enumerate(interval):
        try:
            if interval[k]<interval[k+1]:
                if interval[k]< i <interval[k+1]:
                    first = interval[k+1]-i
                    time.append(['{0}-{1}'.format(interval[k],interval[k+1]),first])
                elif interval[k]< j <interval[k+1]:
                    last = j-interval[k]
                    time.append(['{0}-{1}'.format(interval[k],interval[k+1]),last])
                else:
                    time.append(['{0}-{1}'.format(interval[k],interval[k+1]),100])



                #time.append('{0}-{1}'.format(interval[k],interval[k+1]),100)

        except IndexError:
            pass

    print aoi[count]
    print time
    #print interval
#    print len(interval)-3
    #print interval[1]-i, j-interval[-2]
    mainInt = np.hstack((mainInt, interval))
    count += 1

#print mainInt

test = []
for i,v in enumerate(mainInt):
    try:
        if mainInt[i]<mainInt[i+1]:
            #print '{0}-{1}'.format(mainInt[i],mainInt[i+1])
            test.append('{0}-{1}'.format(mainInt[i],mainInt[i+1]))
    except IndexError:
        pass

#print test


#for i,j in xrange(start.values, end.values):
#    interval = np.arange(i, j, 100)
#    print interval

#print x
#start = np.array(start.values)
#end = np.array(end.values)
#print start.values
#y = np.arange(start,end,100)
#print y

time = 0
new = pd.DataFrame(columns=['Time','% in 1','% in 2','% in 3','% in 4'])
new = pd.DataFrame(columns=['Time','1','2','3','4'])
#new.insert(time,'Time',test)
#print new

trials = data.index.unique()

#print data['CURRENT_FIX_INTEREST_AREAS'][0]

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
'''
