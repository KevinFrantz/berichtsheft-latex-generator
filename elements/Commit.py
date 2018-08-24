import datetime;
class Commit:
    datetime;
    message  = '';
    origin = ''
    def __init__(self,message:str,datetime:datetime):
        self.origin = message
        self.setMessage(message)
        self.datetime = datetime
        self.dayLock = False
    def setMessage(self,message:str):
        self.message = message
    def setDateTime(self,datetime:datetime):
        self.datetime = datetime
    def setDayLock(self):
        #Locks the day for adding other commits
        self.dayLock = True
        #PS: I know that this is not a nice solution ;)
