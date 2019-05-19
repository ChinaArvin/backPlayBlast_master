# -*- coding: utf-8 -*-
class Student(object):
    __slots__ = ('name','age')
    pass

s = Student()
s.name = 'Michael'
s.age = '55'
print s.name,s.age

def set_age(self,age):
    self.age = age

from types import MethodType
Student.set_age = MethodType(set_age,None,Student) #给实列绑定一个方法
s.set_age(25) #调用实列方法

print s.age