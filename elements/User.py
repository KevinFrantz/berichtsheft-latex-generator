from datetime import datetime
class User:
    '''
        This class represents the user
        @author kf
        @since  2018-03-15
    '''
    def __init__(self):
        self.first_name = ''
        self.git_name = ''
        self.git_path = ''
        self.last_name = ''
        self.firma = ''
        self.language = ''
        self.count_start = 0
        self.random_fill_up_datetime = False;
    def setFirstName(self,first_name:str):
        self.first_name = first_name
    def setLastName(self,last_name:str):
        self.last_name = last_name
    def setGitName(self,git_name:str):
        self.git_name = git_name
    def setGitPath(self,git_path:str):
        self.git_path =  git_path
    def setFirma(self,firma:str):
        self.firma = firma
    def setLanguage(self,language:str):
        self.language = language
    def setCountStart(self,count_start:int):
        self.count_start = count_start
    def setRandomFileUp(self,random_fill_up:str):
        if random_fill_up != '':
            self.random_fill_up_datetime = datetime.strptime(random_fill_up, '%Y-%m-%d')
    @property
    def fullName(self):
        return self.first_name + " " + self.last_name
