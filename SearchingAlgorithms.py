def linearsearch(array,element):
    for i in range( len(array)):
        if array[i]==element:
            return('element found at index',i+1)
            break
    return -1
a=[1, 2, 11, 12, 14, 21, 31, 44, 56, 78, 245, 6779]
b=linearsearch(a,10)
print(b)

def binarysearch(array,value):
    beg=0
    end=len(array)-1
    middle=(beg+end)//2
    while not (array[middle]==value) and beg<end:
        if value<array[middle]:
            end=middle-1
        else:
            beg=middle+1
        middle=(beg+end)//2
    if array[middle]==value:
        return middle
    else:
        return -1
c=binarysearch(a,821)
print(c)