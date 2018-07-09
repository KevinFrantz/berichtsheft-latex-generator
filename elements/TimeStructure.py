from datetime import timedelta
from abc import ABC, abstractmethod

class TimeStructureElement(ABC):
    def __init__(self,datetime):
        self.datetime = datetime;
        #self.unadded_commits = []
    @abstractmethod
    def addCommit(self,commit):
        #This method is responsible
        pass
    #def addUnaddedCommit(self,commit):
    #    self.unadded_commits.append(commit)
    #@abstractmethod
    #def getAllUnaddedCommits(self):
    #    pass
#A day containes multiple commits
class Day(TimeStructureElement):
    def __init__(self,datetime):
        self.commits = [];
        super().__init__(datetime);
    def addCommit(self,commit):
        if len(self.commits) < 5:
            print("Add commit '{0}' to weekday {1}...".format(commit.message,self.getWeekday()));
            self.commits.append(commit)
        else:
            print("Commit '{0}' was not added to weekday {1} because the day containes allready more then 5 commits!".format(commit.message,self.getWeekday()));
            #self.addUnaddedCommit(commit)
    def getWeekday(self):
        return self.datetime.weekday();
    def getWeekdayString(self):
        return {
            0:'Monday',
            1:'Thuesday',
            2:'Wednesday',
            3:'Thursday',
            4:'Frieday',
            5:'Saturday',
            6:'Sunday'
        }[self.getWeekday()]

#A week contines multiple days
class Week(TimeStructureElement):
    def __init__(self,datetime):
        self.days = {};
        super().__init__(datetime);
    def addCommit(self,commit):
        print("Add commit '{0}' to week {1}...".format(commit.message,self.getCalenderWeek()));
        dayNumber = commit.datetime.weekday();
        if dayNumber not in self.days:
            self.days[dayNumber] = Day(commit.datetime);
        self.days[dayNumber].addCommit(commit);
    def getFridayDatetime(self):
        return (self.datetime - timedelta(days=(self.datetime.weekday()-6))).strftime('%Y-%m-%d');
    def getMondayDatetime(self):
        #print(self.datetime);
        return (self.datetime - timedelta(days=self.datetime.weekday())).strftime('%Y-%m-%d');
    def getCalenderWeek(self):
        return self.datetime.strftime('%W');

#A year containes out of different weeks
class Year(TimeStructureElement):
    def __init__(self,datetime):
        self.weeks = {};
        super().__init__(datetime);
    def addCommit(self,commit):
        print("Add commit '{0}' to  year {1}...".format(commit.message,self.getYear()));
        weeknumber = commit.datetime.strftime('%W');
        if weeknumber not in self.weeks:
            self.weeks[weeknumber] = Week(commit.datetime);
        self.weeks[weeknumber].addCommit(commit);
    def getYear(self):
        return self.datetime.strftime('%Y');

#This class represents the time structure of the commits:
class TimeStructure:
    def __init__(self):
        self.years = {};
    def addCommit(self,commit):
        print("Add commit '{0}' to timeStructure...".format(commit.message));
        yearNumber = commit.datetime.strftime('%Y');
        if yearNumber not in self.years:
            self.years[yearNumber] = Year(commit.datetime);
        self.years[yearNumber].addCommit(commit);
