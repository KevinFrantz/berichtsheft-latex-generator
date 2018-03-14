#A day containes multiple commits
class Day:
    commits = [];
    #datetime;
    def __init__(self,datetime):
        self.datetime = datetime;
    def addCommit(self,commit):
        self.commits.append(commit);

#A week contines multiple days
class Week:
    days = [];
    #datetime;
    def __init__(self,datetime):
        self.datetime = datetime;
    def addDay(self,day):
        self.days.append(day);
