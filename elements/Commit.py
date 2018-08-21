import datetime;
class Commit:
    datetime;
    message  = '';
    def __init__(self,message:str,datetime):
        self.setMessage(message)
        self.datetime = datetime;
    def setMessage(self,message:str):
        self.message = message
