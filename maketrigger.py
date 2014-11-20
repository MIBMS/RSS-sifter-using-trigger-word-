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
            
def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    
    if triggerType == 'TITLE':
        triggerins = TitleTrigger(''.join(params))
    if triggerType == 'SUBJECT':
        triggerins = SubjectTrigger(''.join(params))
    if triggerType == 'SUMMARY':
        triggerins = SummaryTrigger(''.join(params))        
    if triggerType == 'NOT':    
        triggerins = NotTrigger(triggerMap[params[0]])
    if triggerType == 'AND':
        triggerins = AndTrigger(triggerMap[params[0]],triggerMap[params[1]] )
    if triggerType == 'OR':
        triggerins = OrTrigger(triggerMap[params[0]],triggerMap[params[1]])    
    if triggerType == 'PHRASE':
        triggerins = PhraseTrigger(' '.join(params)) 
  
    triggerMap[name] = triggerins
    return triggerins