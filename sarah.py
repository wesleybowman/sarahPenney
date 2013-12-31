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

data = pd.read_csv('example_data.csv',sep='\t',index_col=0)

trials = data.index.unique()
new = pd.DataFrame()


for trial in trials:
    if trial!=0:
        start = data.loc[trial]['CURRENT_FIX_START']
        end = data.loc[trial]['CURRENT_FIX_END']

        areas = data.loc[trial]['CURRENT_FIX_INTEREST_AREAS']
        areas = areas.values
        aoi = []
        for i in areas:
            areanumbers = re.sub(r'[^\w]', '', i)
            aoi.append(areanumbers)

        count = 0

        for i, j in zip(start.values, end.values):
            start = math.floor(i/100)*100
            end = math.ceil(j/100)*100
            interval = np.arange(start, end+1, 100)

            time = []
            time = sorted(trial,interval,aoi[count])

            time = pd.DataFrame(time)
            time = time.set_index(0)
            new = pd.concat([new,time])

            count += 1

new.columns = ['Time','% in 1','% in 2','% in 3','% in 4']
new.index.name = 'Trial'

grouped = new.groupby([new.index,'Time'],as_index=False).sum()
grouped = grouped.sort(['Time','Trial'])
grouped = grouped.set_index('Trial')

new.to_csv('test.csv')
grouped.to_csv('test2.csv')

averages = new.groupby(new.index).mean()
averages.to_csv('average.csv')
