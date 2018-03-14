from datetime import timedelta

#A day containes multiple commits
class Day:
    commits = [];
    #datetime;
    def __init__(self,datetime):
        self.datetime = datetime;
    def addCommit(self,commit):
        self.commits.append(commit);
    def getWeekday(self):
        return self.datetime.weekday();

#A week contines multiple days
class Week:
    days = [];
    #datetime;
    def __init__(self,datetime):
        self.datetime = datetime;
    def addDay(self,day):
        self.days.append(day);
    def getFridayDatetime(self):
        return (self.datetime - timedelta(days=(self.datetime.weekday()-6))).strftime('%Y-%m-%d');
    def getMondayDatetime(self):
        #print(self.datetime);
        return (self.datetime - timedelta(days=self.datetime.weekday())).strftime('%Y-%m-%d');
    def getCalenderWeek(self):
        return self.datetime.strftime('%W');
