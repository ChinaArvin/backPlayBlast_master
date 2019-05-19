members = 'a.b/c'
obj = members.split('.')[-1].split("/")[0]
print obj
print type(obj)
a = 'c'
if not a in obj:
    print True
