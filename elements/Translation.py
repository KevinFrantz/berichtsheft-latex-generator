from googletrans import Translator
class Translation(object):
    commit_list=[]
    language='en'
    def __init__(self,commit_list:[],language:str):
        self.commit_list=commit_list
        self.language=language
    def routine(self):
        self.pipeThroughTranslationAPI()
        print("Finished translation.")
    def pipeThroughTranslationAPI(self):
        self.iterativ()
    def bulk(self):
        for commit in self.commit_list:
            print("Add commit \"{0}\" to bulk...".format(commit.message))
            bulk.append(commit.message)
            count = count + 1
        print("Translate bulk...")
        translation = Translator()
        translations = translation.translate(bulk, dest=self.language,src='en')
        self.setTranslation(translations)
    def iterativ(self):
        for commit in self.commit_list:
            translation = Translator()
            translation_result = translation.translate(commit.message, dest=self.language,src='en').text
            commit.setMessage(translation_result)
            print("Translated commit {2}/{3} from \"{0}\" to \"{1}\"...".format(commit.origin,commit.message,self.commit_list.index(commit),len(self.commit_list)))
    def setTranslation(self,translations:[]):
        count = 0
        for translated_commit in translations:
            print("Set translation \"{0}\"".format(translated_commit))
            self.commit_list[count].setMessage(translated_commit.text)
            count = count + 1
