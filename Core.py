# @author kf
# @since  2018-03-14
import subprocess;
from elements.Commit import Commit;
from elements.TimeStructure import Day,Week;
import datetime;
class Core:
    def __init__(self,repositoryPath:str):
        self.repositoryPath = repositoryPath;
        self.csvGitLog      = '';
        self.commitGitLog   = [];
        self.timeStructure  = [];
    def exportToCSV(self):
        self.csvGitLog = subprocess.check_output(["git","log",'--pretty=format:%ct,%s']).decode("utf-8");
    def createCommitGitLog(self):
        lines = self.csvGitLog.split("\n");
        for line in lines:
            lineArray   = line.split(",");
            lineCommit  = Commit(lineArray[1],datetime.datetime.fromtimestamp(int(lineArray[0])));
            self.commitGitLog.append(lineCommit);
    def orderTimeStructure(self):
        lastDate    = datetime.datetime.now();
        self.timeStructure = [];
        day         = Day(datetime);
        week        = Week(datetime);
        for commit in self.commitGitLog:
            if int(commit.datetime.strftime('%d')) != int(lastDate.strftime('%d')):
                day = Day(commit.datetime);
            if int(commit.datetime.strftime('%W')) != int(lastDate.strftime('%W')):
                self.timeStructure.append(week);
                week = Week(commit.datetime);
            day.addCommit(commit);
            week.addDay(day);
            lastDate = commit.datetime;
        if week not in self.timeStructure:
            self.timeStructure.append(week);
    def pipeThroughTranslationAPI(self):
        #This function is a dummy right now
        pass;
    def generateLATEXRawFiles(self):
        #This function is a dummy right now
        pass;
    def generateLATEXPdfs(self):
        pass;
