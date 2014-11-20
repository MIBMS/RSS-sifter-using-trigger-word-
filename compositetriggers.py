class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

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