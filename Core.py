# @author kf
# @since  2018-03-14
import subprocess;
import Commit;
class Core:
    def __init__(self,repositoryPath:str):
        self.repositoryPath = repositoryPath;
        self.csvGitLog      = '';
        self.commitGitLog   = [];
    def exportToCSV(self):
        self.csvGitLog = subprocess.check_output(["git","log",'--pretty=format:%cI,%s']).decode("utf-8");
    def createCommitGitLog(self):
        lines = self.csvGitLog.split("\n");
        for line in lines:
            lineArray   = line.split(",");
            lineCommit  = Commit.Commit(lineArray[1],lineArray[0]);
            self.commitGitLog.append(lineCommit);
    def pipeThroughTranslationAPI(self):
        #This function is a dummy right now
        pass;
    def generateLATEXRawFiles(self):
        #This function is a dummy right now
        pass;
    def generateLATEXPdfs(self):
        pass;
