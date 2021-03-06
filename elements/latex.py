import subprocess;
import re;
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
    def newCommand(self,name,content):
        return "\\newcommand{{\\{0}}}{{{1}}}".format(name,content)
    def generateMeta(self):
        document = self.newCommand('Name',self.user.fullName);
        document += self.newCommand('Ausbildungsberuf','Fachinformatiker für Anwendungsentwicklung');
        document += self.newCommand('Firma',self.user.firma)
        self.saveTemplates(document,'Meta')
    def generateLATEXRawFiles(self):
        week_counter = self.user.count_start
        for yearNumber, year in self.timeStructure.years.items():
            document = ""
            for weekNumer,week in year.weeks.items():
                document += "\Titelzeile{{{0}}}{{{1}}}{{{2}}}{{{3}}}".format(week.getMondayDatetime(),week.getFridayDatetime(),yearNumber,week_counter);
                document += '\Woche{';
                for dayNumber,day in week.days.items():
                    document += '\Tag{{{0}}}{{'.format(day.getWeekdayString())
                    document += '\\begin{itemize}'
                    for commit in day.commits:
                        document += "\\item {0}\n".format(self.escape(commit.message));
                    document += '\\end{itemize}'
                    document +='}';
                document += '}';
                document += str('\\Unterschrift{{{0}}}'.format(week.getFridayDatetime()));
                week_counter = int(week_counter) + 1
            self.saveTemplates(document,"Berichte/" + yearNumber)
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
    def escape(self,text):
        characters = {
            r'[^\w]': ' ',
            #'&': r'\&',
            #'%': r'\%',
            #'$': r'\$',
            r'\#':'\\#',
            r'\_':'\_',
            #'{': r'\{',
            #'}': r'\}',
            #'~': r'\textasciitilde{}',
            #'^': r'\^{}',
            #'\\': r'\textbackslash{}',
            #'<': r'\textless{}',
            #'>': r'\textgreater{}',
        }
        for character in characters.keys():
            text = re.sub(character,characters[character],text)
        return text
