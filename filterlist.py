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
# TODO: WordTrigger

# TODO: TitleTrigger
# TODO: SubjectTrigger
# TODO: SummaryTrigger


# Composite Triggers

class NotTrigger(Trigger):
    def __init__(self, other):
        self.other = other
    def evaluate(self, story):
        return not self.other.evaluate(story)
        
class AndTrigger(Trigger):
    def __init__(self, other, other2):
        self.other = other
        self.other2 = other2
    def evaluate(self, story):
        return self.other.evaluate(story) and self.other2.evaluate(story)
        
class OrTrigger(Trigger):
    def __init__(self, other, other2):
        self.other = other
        self.other2 = other2
    def evaluate(self, story):
        return self.other.evaluate(story) or self.other2.evaluate(story)
# Problems 6-8

# TODO: NotTrigger
# TODO: AndTrigger
# TODO: OrTrigger


# Phrase Trigger
# Question 9
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        if self.phrase in story.getTitle() or self.phrase in story.getSubject()\
        or self.phrase in story.getSummary():
            return True
        else:
            return False


'''def filterStories(stories, triggerlist):
    addedstories = []
    for triggerstr in triggerlist:
        ttitle = TitleTrigger(triggerstr)
        tsubject = SubjectTrigger(triggerstr)
        tsummary = SummaryTrigger(triggerstr)
        tphrase = PhraseTrigger(triggerstr)
        for story in stories:
            if ttitle.evaluate(story) or tsubject.evaluate(story) or tsummary.evaluate(story) or tphrase.evaluate(story):
                addedstories.append(story)
    return addedstories'''
    
def filterStories(stories, triggerlist):
    addedstories = []
    for triggerer in triggerlist:
        for story in stories:
            if triggerer.evaluate(story) and story not in addedstories:
                addedstories.append(story)
    return addedstories