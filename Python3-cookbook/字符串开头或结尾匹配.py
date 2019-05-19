#coding:utf-8
# filename = 'spam.text'
# print filename.startswith("spam")
import os
# filename = os.getcwd()
# filenames = os.listdir('..')
# print filenames
# print [name for name in filenames if name.endswith(('.png', '.exe'))]

import re
url = 'http://www.python.org'
result = re.match('http:|https:|ftp:', url)
print url.startswith(('http:','https:','ftp:'))
print url.find('http:')
print result.group()


