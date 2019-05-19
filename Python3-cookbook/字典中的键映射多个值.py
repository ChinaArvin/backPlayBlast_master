from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print d

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print d

d ={}
list = []
d.setdefault("a",list).append(1)



pairs = {"key1":1,"key2":2}
d = defaultdict(list)
for key, value in pairs.items():
    d[key].append(value)
print d


d = {"key1":[1]}
pairs = {"key1":1,"key2":2}
for key, value in pairs.items():
    if key not in d.keys():
        print key
        print d.keys()
        d[key] = []
        d[key].append(value)
print d
