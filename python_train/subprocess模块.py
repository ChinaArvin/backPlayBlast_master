# -*- coding:utf-8 -*-
import  subprocess

print(u'$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print(u'Exit code:',r)