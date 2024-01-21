#tuples are mutable
#tuple are comparable and hashable
new='a','b','c'
print(type(new))
m=('a',)
print(m)
m=tuple()
print(m)
print(new[0:])
#traversing
for index,value in enumerate(new):
    print(index,value)
#searching
val='9'
for index,value in enumerate(new):
    if val==value:
        print(index,value)
        break
else:
    print('not found')
new1=('d','e')
a=new+new1#concatenation
print(a)
print(a*23) #replication
print(a.count('b'))
print(a.index('b'))

