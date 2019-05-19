# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2014 - self._birth
# s = Student()
# s.birth = 5
# print(s.age)
import os
currentPath = os.path.dirname(__file__)
print currentPath