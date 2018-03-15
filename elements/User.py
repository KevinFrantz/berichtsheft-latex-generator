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
    def setFirstName(self,first_name:str):
        self.first_name = first_name
    def setLastName(self,last_name:str):
        self.last_name = last_name
    def setGitName(self,git_name:str):
        self.git_name = git_name
    def setGitPath(self,git_path:str):
        self.git_path =  git_path
