import datetime
class RandomFillUp(object):
    def __init__(self,timeStructure,user):
        self.timeStructure = timeStructure
        self.user = user
    def fillUpFromLastCommit(self):
        unadded_commits_count = 0;
        count_datetime = self.timeStructure.getOldestCommit().datetime
        while(self.timeStructure.getOldestCommit().datetime<self.user.random_fill_up_datetime):
            count_datetime = count_datetime + datetime.timedelta(days=1)
            if count_datetime.weekday() not in [5,6]:
                day_commit_count=0
                while(day_commit_count<5):
                    commit = self.timeStructure.getAllUnaddedCommits()[unadded_commits_count]
                    commit.setDateTime(count_datetime)
                    self.timeStructure.addCommit(commit)
                    unadded_commits_count = unadded_commits_count + 1
                    day_commit_count = day_commit_count + 1
