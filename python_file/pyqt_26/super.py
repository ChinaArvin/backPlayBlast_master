# -*- coding: utf-8 -*-
# super 调用父类的方法
class A(object): # 父类也必须继承点什么东西 否则super函数识别不出来
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add',format(self))
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def add(self , m):
        print('self is {0} @B.add', format(self))
        super(B ,self).add(m)
        #self.n += 3
a = A()
a.add(2)
print(a.n)

b = B()
b.add(2)
print(b.n)