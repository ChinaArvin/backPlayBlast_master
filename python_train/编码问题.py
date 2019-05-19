# coding=utf-8
s='中文'

if(isinstance(s, str)):
# s为u'中文'
    print type(s)
    print type(s.encode('gb2312'))
    print type(s.decode('utf8').encode('gb2312'))
else:
# s为'中文'
    print s.decode('utf8').encode('gb2312')