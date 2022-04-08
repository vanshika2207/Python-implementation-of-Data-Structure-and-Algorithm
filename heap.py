largest=0
def heapify(aaray,size,i):
    i=largest
    left_child=2*i+1
    right_child=2*i+2
    if array[left_child]>array[i] and left_child<size:
        left_child=largest
    if array[right_child]>array[i] and right_child<size:
        right_child=largest
    if largest !=i:
        array[i],array[largest]=array[largest],array[i]
        heapify(array,n,largest)
def insert(array,newnumber):
    size=len(array)
    if size==0:
        array.append(newnumber)
    else:
        array.append(newnumber)
        for i in range((size//2)-1,-1,-1):
            heapify(array,size,i)
def delete(array,number):
    size=len(array)
    i=0
    for i in range(0, size):
        if number == array[i]:
            break
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(number)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)    
array=[]        
insert(array, 3)
insert(array, 9)
insert(array, 2)
insert(array, 1)
insert(array, 4)
insert(array,5)
print ("Max-Heap array: " + str(array))

delete(array, 4)
print("After deleting an element: " + str(array))
