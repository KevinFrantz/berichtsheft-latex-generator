# @author kf
# @since  2018-03-14
import subprocess
import pathlib
import datetime
from elements.latex import Compiler
from elements.Commit import Commit
from elements.TimeStructure import TimeStructure
from elements.Filter import Filter
from elements.Translation import Translation
from elements.RandomFillUp import RandomFillUp
from elements.Events import Events

class Core:
    def __init__(self,user):
        self.user           = user
        self.csvGitLog      = ''
        self.commit_list   = []
        self.timeStructure  = TimeStructure()
    def routine(self):
        self.exportToCSV()
        self.createCommitList()
        self.filter()
        if(self.user.language!=''):
            self.translate()
        self.orderTimeStructure()
        if pathlib.Path("events.csv").exists():
            self.events()
        if(self.user.random_fill_up_datetime):
            self.randomFillUpTimeStructure();
        self.printPreview()
        self.compile()
    def compile(self):
        print("Initialize LaTeX Compiler...")
        compiler = Compiler(self)
        print("Start compiling routine...")
        try:
            compiler.generationRoutine()
        except subprocess.CalledProcessError:
            print("\nATTENTION: The compiler returned a non-zero exit status.\nMay this is a problem ¯\_(ツ)_/¯\n\n")
        print("The compiling process finished •ᴗ• ")
    def exportToCSV(self):
        print("Export commits to CSV...")
        self.csvGitLog = subprocess.check_output(["git","log",'--pretty=format:%ct,%s','--author={0}'.format(self.user.git_name)],cwd=self.user.git_path).decode("utf-8");
    def createCommitList(self):
        print("Transfers the CSV to a commit list...")
        lines = self.csvGitLog.split("\n");
        for line in lines:
            lineArray   = line.split(",");
            lineCommit  = Commit(lineArray[1],datetime.datetime.fromtimestamp(int(lineArray[0])));
            self.commit_list.append(lineCommit)
    def orderTimeStructure(self):
        print("Creates the commit time structure... ")
        for commit in self.commit_list:
            self.timeStructure.addCommit(commit);
        self.timeStructure.sort()
    def randomFillUpTimeStructure(self):
        print("File up dates till {0} ...".format(self.user.random_fill_up_datetime.strftime("%Y-%m-%d")))
        randomFillUp = RandomFillUp(self.timeStructure,self.user)
        randomFillUp.fillUp()
    def printPreview(self):
        print("\n\n\n Preview:\n\n")
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
        translate_modul.routine()
    def events(self):
        print("Set event commits...")
        events = Events(self.timeStructure)
        events.setCommits()
