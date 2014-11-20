import string

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
        
    def isWordIn(self, text):
        text = text.lower()
        for i in string.punctuation:
            text = text.replace(i, " ")         
        txtlist = text.split()
        if self.word.lower() in txtlist:
            return True
        else:
            return False

class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        title1 = story.getTitle()
        return WordTrigger.isWordIn(self, title1)

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        subject1 = story.getSubject()
        return WordTrigger.isWordIn(self, subject1)
        
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        summary1 = story.getSummary().lower()
        return WordTrigger.isWordIn(self, summary1)    