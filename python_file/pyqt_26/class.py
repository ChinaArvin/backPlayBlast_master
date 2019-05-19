# -*- coding: utf-8 -*-
class Student(object):

    def __init__(self,name, score):
        # 数据
        self.name = name
        self.score = score

    def  print_score(self):
        # 内部定义访问数据函数
         print("%s: %s" % (self.name , self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        if self.score >= 60:
            return  'B'
        else:
            return 'C'


bart = Student('Bart Simpson',59)
bart.print_score()

def print_score(std):
    ''' 面向对象编程的一个重要特点就是数据封装。在上面的Student类中，
    每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据(外部访问) '''
    print("%s: %s" %(std.name,std.score))

print_score(bart)

lisa = Student('Lisa',90)
print (lisa.name ,lisa.get_grade())