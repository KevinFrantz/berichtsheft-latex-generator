# @author kf
# @since  2018-03-14
import subprocess;
class Core:
    def __init__(self,repositoryPath):
        self.repositoryPath = repositoryPath;
        self.csvGitLog      = '';
    def exportToCSV(self):
        self.csvGitLog = subprocess.check_output(["git","log",'--pretty=format:%cI,%h,%an,%ae,%s']);
    def cleanCSV(self):
        cleanCSV = [];
        print("test {0}".format(self.csvGitLog));
        lines = self.csvGitLog.split("\n");
        for line in lines:
            print(line);
    def getCSV(self):
        return self.csvGitLog;
    def pipeThroughTranslationAPI(self):
        #This function is a dummy right now
        pass;
    def generateLATEXRawFiles(self):
        #This function is a dummy right now
        pass;
    def generateLATEXPdfs(self):
        pass;
