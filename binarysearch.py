a=eval(input("enter the list you want to enter"))
print(a)
length=len(a)
item=int(input("enter the item you want to search"))
beg=0
end=length-1
mid=int((beg+end)/2)
while beg<=end:
    if a[mid]==item:
        print("item found ,at position :",mid+1)
        break
    elif a[mid]>item:
         end=mid-1
         mid=int((beg+end)/2)
    else:
        beg=mid+1
        mid=int((beg+end)/2)
else:
    print("item not found")
    
