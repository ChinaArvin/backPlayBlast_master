# a = [i for i in range(4)]
# # print a

# f = [lambda x:x*i for i in range(4)]
# print f[0]

# def func():
#     fun_list = []
#     for i in range(4):
#         print "No.1:" ,i
#         def foo(x,i = i):
#             print "No.2:" , i
#             return x*i
#         fun_list.append(foo)
#     return fun_list
#
# for m in func():
#     print m(2)

f1 =[lambda x=1,i=i: x*i for i in range(4)]
for f in f1:
    print f(1)