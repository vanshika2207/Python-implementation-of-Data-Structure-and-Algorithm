#recursive binary search
def binarySearch(array,i,l,x):
    if(l==i):
        if(x==array[i]):
            print("element found at", i+1)
        else:
            print("element not found")
    else:
        mid=int((i+l)/2)
        if(x==array[mid]):
            print(mid+1)
            return mid
        elif(x<array[mid]):
            return binarySearch(array,i,mid-1,x)
        else:
            return binarySearch(array, mid+1, l, x)
array=eval(input("enter array"))
x=int(input("enter element you want to search"))
i=0
l=len(array)
binarySearch(array, i, l, x)       
        
