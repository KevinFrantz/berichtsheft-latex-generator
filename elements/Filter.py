import re;
class Filter(object):
    """
    This class filters text
    """
    commit_list = []
    def __init__(self,commit_list):
        self.commit_list = commit_list
    def routine(self):
        for commit in self.commit_list:
            commit.setMessage(self.escape(commit.message))
    def escape(self,text):
        words = {
            'refs #':'ticket ',
            '\:\)':'',
            '\;\)':'',
            '\<\/':'',
            '\>':'',
            '\{\%':'',
            '\%\}':'',
            '\-\.\-':'',
        }
        for word in words.keys():
            text = re.sub(word,words[word],text)
        return text
