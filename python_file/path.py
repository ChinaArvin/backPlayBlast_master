import os
[x for x in os.listdir(".")if os.path.isfile(x) and os.path.splitext(x)[1]==".py"]
x = x.decode('unicode_escape')
print x
print os.path.abspath(".")


