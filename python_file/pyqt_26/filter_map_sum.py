def f(x) :
    return x % 3 == 0 or x % 5 == 0
filter(f,range(2,25))
print(filter(f,range(2,25)))

def q(x) :
    return x*x*x

map(q,range(2,11))
print(map(q,range(2,11)))

for i in range(1,11):
    print i,

def sum(seq):
    def add(x,y): return x+y
    return reduce(add,seq,0)

print(sum(range(1,11)))
print(sum([1,2,3]))

def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
