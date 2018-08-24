import datetime
class RandomFillUp(object):
    def __init__(self,timeStructure,user):
        self.timeStructure = timeStructure
        self.user = user
        self.__setFrom()
        self.__setTill()
    def __setFrom(self):
        if(self.user.random_fill_up_from_datetime):
            self.from_datetime = self.user.random_fill_up_from_datetime
        else:
            self.from_datetime = self.timeStructure.getFirstCommit().datetime
    def __setTill(self):
        if(self.user.random_fill_up_datetime):
            self.till_datetime = self.user.random_fill_up_datetime
        else:
            self.till_datetime = self.timeStructure.getOldestCommit().datetime
    def fillUp(self):
        unadded_commits_count = 0;
        count_datetime = self.from_datetime
        while(count_datetime<self.till_datetime):
            count_datetime = count_datetime + datetime.timedelta(days=1)
            if count_datetime.weekday() not in [5,6]:
                day_commit_count=0
                while(day_commit_count<5):
                    if(unadded_commits_count>=len(self.timeStructure.getAllUnaddedCommits())):
                        unadded_commits_count=0
                    commit = self.timeStructure.getAllUnaddedCommits()[unadded_commits_count]
                    commit.setDateTime(count_datetime)
                    self.timeStructure.addCommit(commit)
                    unadded_commits_count = unadded_commits_count + 1
                    day_commit_count = day_commit_count + 1
        self.timeStructure.sort();
