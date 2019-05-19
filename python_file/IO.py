try:
    import cPickle as pickle
except ImportError:
    import pickle

d= dict(name = "Bob",age = "20",score = "80")
print(type(d))
pickle.dumps(d)
f = open("dump.txt","wb")
pickle.dump(d,f)
f.close()