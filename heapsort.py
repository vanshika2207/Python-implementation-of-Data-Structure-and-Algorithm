def heapify(array,size,i):
    largest=i
    left_child=2*i+1
    right_child=2*i+2
    if  left_child<size and array[i]<array[left_child]:
        largest=left_child
    if right_child<size and array[largest]<array[right_child]:
        largest=right_child 
    if largest !=i:
        array[i],array[largest]=array[largest],array[i]
        heapify(array,size,largest)
def heapsort(array):
    size=len(array)
    for i in range (size//2-1,-1,-1):
        heapify(array,size,i)
    for i in range(size-1,0,-1):
        array[i],array[0]=array[0],array[i]
        heapify(array,i,0)
        

arr=eval(input("enter array"))
 
heapsort(arr)
size=len(arr) 
print(arr)
