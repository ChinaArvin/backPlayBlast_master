import yaml

objects = {"name":"limengen",
           "age":"22",
           "sex":"man",
           "childen":[{"relation":"son"},{"relation":"daughter"}]}
print yaml.dump(object)

# with open("ouput.yaml","w") as f:
#     print yaml.dump(objects,f)