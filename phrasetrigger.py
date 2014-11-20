class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError
        
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        if self.phrase in story.getTitle() or self.phrase in story.getSubject()\
        or self.phrase in story.getSummary():
            return True
        else:
            return False