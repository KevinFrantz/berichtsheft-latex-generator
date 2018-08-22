import sys
import argparse
from Core import Core
from elements.User import User;
class Main(object):
    def __init__(self):
        self.parser()
        self.setUser()
        self.core()
    def core(self):
        core=Core(self.user)
        core.routine()
    def setUser(self)->User:
        self.user=User();
        self.user.setGitPath(self.args.path)
        self.user.setGitName(self.args.user)
        self.user.setFirstName(self.args.first_name)
        self.user.setLastName(self.args.last_name)
        self.user.setFirma(self.args.company)
        self.user.setCountStart(self.args.count_start)
        self.user.setLanguage(self.args.translation)
        self.user.setRandomFileUp(self.args.random_fill_up)
    def parser(self):
        parser = argparse.ArgumentParser(description='Generates reports based on a git repository')
        parser.add_argument('--path', help='The path to the git repository')
        parser.add_argument('--user', help='The git user')
        parser.add_argument('--first-name', help='The first name of the user')
        parser.add_argument('--last-name', help='The last name of the user')
        parser.add_argument('--company', help='The company')
        parser.add_argument('--count-start', default=1, help='Number from which the counting should start')
        parser.add_argument('--translation', default='', help='Language to which the reports should be translated trough')
        parser.add_argument('--random-fill-up', default='', help='Time to which logs should be filled up with random commits')
        self.args = parser.parse_args()
Main()
