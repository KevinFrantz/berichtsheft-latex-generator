# @author kf
# @since  2018-03-14
import subprocess
from elements.latex import Compiler
from elements.Commit import Commit
from elements.TimeStructure import TimeStructure
from elements.Filter import Filter
from elements.Translation import Translation
import datetime
class Core:
    def __init__(self,user):
        self.user           = user
        self.csvGitLog      = ''
        self.commit_list   = []
        self.timeStructure  = TimeStructure()
    def routine(self):
        print("Export commits to CSV...")
        self.exportToCSV()
        print("Transfers the CSV to a commit list...")
        self.createCommitList()
        self.filter()
        if(self.user.language!=''):
            print("Translates commits...")
            self.translate()
        print("Creates the commit time structure... ")
        self.orderTimeStructure()
        if(self.user.random_fill_up_datetime):
            print("File up dates till {0} ...".format(self.user.random_fill_up_datetime.strftime("%Y-%m-%d")))
            self.randomFillUpTimeStructure();
        print("\n\n\n Commits Time Structure:\n\n")
        self.printPreview()
        print("Initialize LaTeX Compiler...")
        compiler = Compiler(self)
        print("Start compiling routine...")
        try:
            compiler.generationRoutine()
        except subprocess.CalledProcessError:
            print("\nATTENTION: The compiler returned a non-zero exit status.\nMay this is a problem ¯\_(ツ)_/¯\n\n")
        print("The compiling process finished •ᴗ• ")
    def exportToCSV(self):
        self.csvGitLog = subprocess.check_output(["git","log",'--pretty=format:%ct,%s','--author={0}'.format(self.user.git_name)],cwd=self.user.git_path).decode("utf-8");
    def createCommitList(self):
        lines = self.csvGitLog.split("\n");
        for line in lines:
            lineArray   = line.split(",");
            lineCommit  = Commit(lineArray[1],datetime.datetime.fromtimestamp(int(lineArray[0])));
            self.commit_list.append(lineCommit)
    def orderTimeStructure(self):
        for commit in self.commit_list:
            self.timeStructure.addCommit(commit);
        self.timeStructure.sort()
    def randomFillUpTimeStructure(self):
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
    def printPreview(self):
        for yearNumber, year in self.timeStructure.years.items():
            print("Jahr {0} ".format(year.getYear()));
            for weekNumer,week in year.weeks.items():
                print("Woche {0} vom {1} bis {2}".format(week.getCalenderWeek(),week.getMondayDatetime(),week.getFridayDatetime()));
                for dayNumber,day in week.days.items():
                    print("Tag {0}".format(day.getWeekday()));
                    for commit in day.commits:
                        print("- {0}".format(commit.message));
    def filter(self):
        print("Filtering commits...")
        filter_modul = Filter(self.commit_list)
        filter_modul.routine();
    def translate(self):
        print("Translate commits...")
        translate_modul = Translation(self.commit_list,self.user.language)
        translate_modul.routine();
