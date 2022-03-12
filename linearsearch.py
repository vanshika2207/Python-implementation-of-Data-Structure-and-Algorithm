a=eval(input("enter the list you want to enter"))
print(a)
length=len(a)
item=int(input("enter the item you want to searxh"))
flag=0
position=0
for i in range(0,length):
    if a[i]==item:
        flag=1
        position=i
        break
if flag==0:
    print("item is not in the list")
else:
    print("item is found at position :",position+1)
        
    
        
