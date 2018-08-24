import csv
import datetime
from .Commit import Commit

class Events(object):
    def __init__(self,timeStructure):
        self.file = 'events.csv'
        self.timeStructure = timeStructure
    def setCommits(self):
        with open(self.file, newline='') as csvfile:
            event_csv = csv.reader(csvfile, delimiter=';', quotechar='|')
            for event in event_csv:
                self.__eventRoutine(datetime.datetime.strptime(event[0],'%Y-%m-%d'),datetime.datetime.strptime(event[1],'%Y-%m-%d'),event[2])
    def __eventRoutine(self,start_datetime:datetime.datetime,end_datetime:datetime.datetime,message):
        date_count = start_datetime
        while(date_count<=end_datetime):
            if date_count.weekday() not in [5,6]:
                self.__setCommit(date_count,message)
            date_count = date_count + datetime.timedelta(days=1)
    def __setCommit(self,datetime,message:str):
        commit = Commit(message,datetime)
        commit.setDayLock()
        self.timeStructure.addCommit(commit)
