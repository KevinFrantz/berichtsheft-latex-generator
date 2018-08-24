import datetime;
class Commit:
    datetime;
    message  = '';
    origin = ''
    def __init__(self,message:str,datetime:datetime):
        self.origin = message
        self.setMessage(message)
        self.datetime = datetime
    def setMessage(self,message:str):
        self.message = message
    def setDateTime(self,datetime:datetime):
        self.datetime = datetime
