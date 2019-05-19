# -*- coding: utf-8 -*-

fo = open('foo.txt','w')
fo.write('www.runoob.com!\nVery good site!\n')

fo = open('foo.txt','r+')
str = fo.read(10)

print str

position = fo.tell()
print position

position = fo.seek(0,0)
str = fo.read(10)
print str

fo.close()



