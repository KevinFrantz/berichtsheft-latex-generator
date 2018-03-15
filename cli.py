import sys
from Core import Core
from elements.User import User;
user=User();
if len(sys.argv) < 2:
    ''' @hint The first argv element containes the path of the file.'''
    print("CLI - BLG \nBerichtsheft LaTeX Generator\n@author kf\n@since 2018-03-05\n\nPlease insert the parameters ;)\n");
    user.setGitPath(input("Please type in the path of the git-repository:"))
    user.setGitName(input("Please insert the name of the git-author which should be used:"))
    user.setFirstName(input("Please insert your first name:"))
    user.setLastName(input("Please insert your last name:"))
    user.setFirma(input("Please insert the name of your company:"))
else:
    try:
        user.setGitPath(sys.argv[1])
        user.setGitName(sys.argv[2])
        user.setFirstName(sys.argv[3])
        user.setLastName(sys.argv[4])
        user.setFirma(sys.argv[5])
    except IndexError:
        print("You didn't pass all needed parameters :( \nPlease try again :) :) :)")
core=Core(user)
core.routine()
