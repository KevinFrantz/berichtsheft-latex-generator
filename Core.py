# @author kf
# @since  2018-03-14
import subprocess;
from elements.Commit import Commit;
from elements.TimeStructure import TimeStructure;
import datetime;
class Core:
    def __init__(self,repositoryPath:str):
        self.repositoryPath = repositoryPath;
        self.csvGitLog      = '';
        self.commitGitLog   = [];
        self.timeStructure  = TimeStructure();
    def exportToCSV(self):
        self.csvGitLog = subprocess.check_output(["git","log",'--pretty=format:%ct,%s'],cwd=self.repositoryPath).decode("utf-8");
    def createCommitGitLog(self):
        lines = self.csvGitLog.split("\n");
        for line in lines:
            lineArray   = line.split(",");
            lineCommit  = Commit(lineArray[1],datetime.datetime.fromtimestamp(int(lineArray[0])));
            self.commitGitLog.append(lineCommit);
    def orderTimeStructure(self):
        print("Iterate over commit list...");
        for commit in self.commitGitLog:
            self.timeStructure.addCommit(commit);
    def generateBerichtsheft(self):
        for yearNumber, year in self.timeStructure.years.items():
            print("Jahr {0} ".format(year.getYear()));
            for weekNumer,week in year.weeks.items():
                print("Woche {0} vom {1} bis {2}".format(week.getCalenderWeek(),week.getMondayDatetime(),week.getFridayDatetime()));
                for dayNumber,day in week.days.items():
                    print("Tag {0}".format(day.getWeekday()));
                    for commit in day.commits:
                        print("- {0}".format(commit.message));

    def pipeThroughTranslationAPI(self):
        #This function is a dummy right now
        pass;
    def generateLATEXRawFiles(self):
        #This function is a dummy right now
        pass;
    def generateLATEXPdfs(self):
        pass;
