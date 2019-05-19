text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re

# print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# print datepat.sub(r"\3-\1-\2",text)

text = 'UPPER PYTHON, lower python, Mixed Python'
# print re.findall('python',text,flags=re.IGNORECASE)

