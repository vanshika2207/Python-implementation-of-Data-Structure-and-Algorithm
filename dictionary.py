#create a dictionary
mydict=dict()
print(mydict)
mydict={}
print(mydict)
engtosp={'one':'uno','two':'dos','three':'tres'}
print(engtosp)
a=engtosp['one']
print(a)
# b=engtosp['four']
# print(b)
#accessing -o(1)
##dictionary in memory
#associative array use hash function

#dictionary are mutable
##updating the value in dictionary
engtosp['four']='char'
print(engtosp)
engtosp['three']='teen'
#o(1)
print(engtosp)
print(hash(engtosp['four']))
#traversing the dictionary
for key,value in engtosp.items():
    print(key,value)
#o(n)
#searching element in the dictionary
val='chiar'
for key,value in engtosp.items():
    if value==val:
        print(key,value)
        break

else:
    print('not found')
#o(n)
a=engtosp.pop('four')
print(a)
a=engtosp.popitem()
print(a)
a=engtosp.setdefault('one','not found')
print(a)
engtosp.clear()
print(engtosp)
del engtosp
#o(1)
##more dictionary methods
a={'name':'vanshika saxena','age':20,'year':3}
b=a.copy() #deep copy
print(b)
b['age']=21
print(a)
print(b)
print(id(a),id(b))
c=a #shallow copy
print(id(c),id(a))
c['age']=21
print(a)
a1={}.fromkeys([1,2,3],0)
print(a1)
print(a.get('age1','does not exist'))
print(a)
print(a.setdefault('class','datascience'))
print(a)
a.update({'age':23})
print(a)

