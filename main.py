#!/bin/python
import Core;
from pprint import pprint
#gitPath = input("Please type in the path of the git-repository:");
gitPath = r'/home/kevinfrantz/repositories/kevinfrantz.github/berichtsheft-latex-generator';
print("The programm will use \"{0}\" as repository path.".format(gitPath));
core = Core.Core(gitPath);
core.exportToCSV();
core.createCommitGitLog();
core.orderTimeStructure();
#pprint(core.timeStructure[0].days);
#pprint(core.timeStructure[0].days);
#core.generateBerichtsheft();
pprint(core.timeStructure.years['2018'].weeks['11'].days[3].commits);
