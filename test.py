import string

def evaluate(text, word):
        for i in string.punctuation:
            text = text.replace(i, " ")                   
        txtlist = text.split()
        if word in txtlist:
            return True
        else:
            return False
            
print evaluate('I prefer pillows that are soft.', 'soft')