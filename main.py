#!/bin/python
import Core;
#gitPath = input("Please type in the path of the git-repository:");
gitPath = 'test';
print("The programm will use \"{0}\" as repository path.".format(gitPath));
core = Core.Core(gitPath);
core.exportToCSV();
core.createCommitGitLog();
print(core.commitGitLog[1].message);
