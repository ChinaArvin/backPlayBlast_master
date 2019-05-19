import re
text = 'UPPER PYTHON, lower python, Mixed Python'

def matchcase(word):
    def replace(a):
        text = a.group()
        print text
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print  re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)