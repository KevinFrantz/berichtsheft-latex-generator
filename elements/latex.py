import subprocess;
class Compiler:
    '''
    This compiler translates the core to LaTeX
    @author kf
    @since 2018-03-15
    '''
    template_folder="templates/LaTeX-Vorlage-Berichtsheft/";
    def __init__(self,core):
        self.timeStructure = core.timeStructure;
        self.user = core.user
    def generationRoutine(self):
        self.generateMeta()
        self.generateLATEXRawFiles()
        self.generateMainFile()
        self.generateLATEXPdfs()
    def generateMeta(self):
        document = "\\newcommand{{\\Name}}{{{0}}}".format(self.user.fullName)
        document += "\\newcommand{\\Ausbildungsberuf}{Fachinformatiker für Anwendungsentwicklung}"
        self.saveTemplates(document,'Meta')
    def generateLATEXRawFiles(self):
        document = ""
        for yearNumber, year in self.timeStructure.years.items():
            document += "\Titelzeile{{Juli}}{{{0}}}{{18}}".format(yearNumber);
            for weekNumer,week in year.weeks.items():
                document += '\Woche{';
                for dayNumber,day in week.days.items():
                    document += '\Tag{{{0}}}{{'.format(dayNumber);
                    for commit in day.commits:
                        document += "{0}\n".format(commit.message);
                    document +='}';
                document += '}';
            document += str("\\Unterschrift");
            self.saveTemplates(document,"Berichte/" + yearNumber);
    def generateMainFile(self):
        document = '\documentclass[ngerman]{scrreprt}'
        document += '\input{Packages}'
        document += '\input{Befehle}'
        document += '\input{Meta}'
        document += '\\begin{document}'
        for yearNumber in self.timeStructure.years:
            document += '\include{{Berichte/{0}}}'.format(yearNumber);
        document += '\end{document}'
        self.saveTemplates(document,'Berichtsheft');
    def saveTemplates(self,content,name):
        file = open(self.template_folder + "/{0}.tex".format(name),"w+");
        lines = content.split("\n");
        for line in lines:
            file.write(line);
        file.close();
    def generateLATEXPdfs(self):
        print(subprocess.check_output(["texliveonfly","Berichtsheft.tex"],cwd=self.template_folder).decode("utf-8"));
