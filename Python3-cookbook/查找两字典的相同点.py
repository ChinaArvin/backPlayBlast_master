a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print list(set(a.items())&set(b.items()))
c = {key:a[key] for key in set(a.keys()) - {'z','w'}}
print c


print set(a.keys())&set(b.keys()) # python2
# print a.keys()&b.keys() python3


x = set('spam')
y = set(['h','a','m'])

print x&y