import json
import yaml

# data = {'a':1 , 'b':2}
#
# s = json.dumps(data)
# print type(s)
#
# print json.loads(s)
#
# print type(json.loads(s))
#
# new = json.loads(s)
#
# print  new['b']


person_dict = {'a':1,'b':2,'number':[1,1,2]}

with open("test.json","w") as f:
    f.write(json.dumps(person_dict,indent=4))

with open("D:\Maya_film\Maya2018\Material/test.json","r") as f:
    a=json.load(f)
print type(a)

