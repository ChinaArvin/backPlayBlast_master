def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
p = sorted(['bob','about','Zoo'],cmp_ignore_case)
print(p)

z = sorted(['bob','about','Zoo'],reverse = True)
print(z)

def cmp_ignore_case1(s1,s2):
    u1 = s1[0][0].upper()
    u2 = s2[0][0].upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0

students = [('bob','A',15),('about','B',12),('Zoo','B',10)]
q = sorted(students,cmp_ignore_case1)
print(q)