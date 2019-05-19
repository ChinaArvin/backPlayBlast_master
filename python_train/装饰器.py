# def log(text):
#     def decorator(func):
#         def wrapper(*argv,**kw):
#             print ("%s call %s:" % (text,func.__name__))
#             return func(*argv,**kw)
#         return wrapper
#     return decorator
#
# @log("execute")
# def now():
#     print("2019-4-15")
#
# now()

# -*- coding: utf-8 -*-
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__,10.24))
        return fn(*args,**kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
print f
s = slow(11, 22, 33)
print s
if f != 33:
    print('error!')
elif s != 7986:
    print('error!')

