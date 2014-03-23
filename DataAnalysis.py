from __future__ import division
import numpy as np
import pandas as pd
import math
import re
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import os

'''The sorted function arranges things by areas of interest.'''
def sortedData(trial,interval,time,aoi,i,j):
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



'''fixData functions takes in the files, one at a time, and fixes them to how
they are wanted for the output. It also saves the output file with the
specified name, and returns the averaged file so it can be correctly appended
and outputted. '''
def fixData(file, saveAs, includeStart=False, includeStop=False):

    try:
        data = pd.read_csv(file,sep='\t')
    except pd.parser.CParserError:
        data = pd.read_excel(file,0)

    data = data.set_index('trial_count')

    trials = data.index.unique()
    new = pd.DataFrame()

    for trial in trials:
        if trial!=0:
            start = data.loc[trial]['CURRENT_FIX_START']
            end = data.loc[trial]['CURRENT_FIX_END']

            startValues = data.loc[trial]['verb_onset'].values[-1]
            startValues = math.floor(startValues/100)*100

            stopValues = data['Sentence_duration_ms'].dropna()
            stopValues = math.floor(stopValues.values[trial-1]/100)*100

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

                try:
                    if lastInterval not in interval:
                        newInterval = np.arange(lastInterval,interval[0]+1,100)

                        if includeStart:
                            ind = np.where(newInterval>=startValues)[0]
                            newInterval = newInterval[ind]

                        if includeStop:
                            ind = np.where(newInterval<=stopValues)[0]
                            newInterval = newInterval[ind]

                        newInterval = list(newInterval)

                        if newInterval:
                            time = []
                            time = sortedData(trial,newInterval,time,'',i,j)

                            try:
                                time = pd.DataFrame(time)
                                time = time.set_index(0)
                                new = pd.concat([new,time])
                            except KeyError:
                                pass

                except:
                    pass

                lastInterval = interval[-1]

                if includeStart:
                    ind = np.where(interval>=startValues)[0]
                    interval = interval[ind]

                if includeStop:
                    ind = np.where(interval<=stopValues)[0]
                    interval = interval[ind]

                time = []
                time = sortedData(trial,interval,time,aoi[count],i,j)

                try:
                    time = pd.DataFrame(time)
                    time = time.set_index(0)
                    new = pd.concat([new,time])
                except KeyError:
                    pass

                count += 1

    new.columns = ['Time','% in 1','% in 2','% in 3','% in 4']
    new.index.name = 'Trial'

    grouped = new.groupby([new.index,'Time'],as_index=False).sum()

    grouped[['start', 'end']] = grouped['Time'].apply(lambda val: pd.Series(map(float, val.split('-'))))
    grouped.sort(['Trial','start', 'end'], inplace=True)
    grouped = grouped.set_index('Trial')

    #Here we have a start and end column, which allows us to sort
    #Can keep that or get rid of it
    newData = grouped.drop(['start','end'],1)

    #Write all of the data to files
    #new.to_csv('test.csv')
    #grouped.to_csv('test2.csv')
    newData.to_csv(saveAs)

    averages = new.groupby(new.index).mean()
    #averages.to_csv('average.csv')

    return averages

'''the main function is just the GUI for inputting files, and regular
expressions for naming the files. It also handles concatinating all of the
averaged files together, so that only one averaged file is outputted.'''
def main():
    app = QApplication(sys.argv)
    caption = 'Open Files'
    directory = './'
    #Do we need to delete old files?
    files = QFileDialog.getOpenFileNames(None, caption, directory)[0]

    averaged = pd.DataFrame()

    ifStart = raw_input('\nDo you want to include Verb Onset? ')

    ifStop = raw_input('\nDo you want to include Sentence Duration? ')

    for file in files:
        saveAs, ext=os.path.splitext(file)
        match = re.search('\d{1,2}',saveAs)
        saveAs = match.group(0)
        saveAs = 'participant#{0}.csv'.format(saveAs)
        averageName = 'participantsAveraged.csv'

        averages = fixData(file, saveAs, ifStart, ifStop)

        saveAs = saveAs.split('/')
        nameSpacer = pd.DataFrame({'Name':[saveAs[-1]]})

        averaged = pd.concat([averaged,nameSpacer])
        averaged = pd.concat([averaged,averages])

        averaged.to_csv(averageName)

if __name__ == '__main__':
    main()
