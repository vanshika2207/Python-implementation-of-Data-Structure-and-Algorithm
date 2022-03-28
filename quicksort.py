
def pivot(array, start, end):
 
#initializing 
    pivot = array[start]
    low = start +1
    high = end
 
 
    while True:
   
#moving high towards left
        while low <= high and array[high] >= pivot:
            high = high - 1
 
#moving low towards right 
        while low <= high and array[low] <= pivot:
            low = low + 1
 
#checking if low and high have crossed
        if low <= high:
 
#swapping values to rearrange
            array[low], array[high] = array[high], array[low]
          
        else:
#breaking out of the loop if low > high
            break
 
#swapping pivot with high so that pivot is at its right # #position 
    array[start], array[high] = array[high], array[start]
 
#returning pivot position
    return high

def quick_sort(array, start, end):
    if start >= end:
        return
    p = pivot(array, start, end)
    print("Pivot",array[p])
    print("left :", array[start:p])
    print("right :",array[p+1:end+1])
    print("\n")
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
array = [50,30,10,90,80,20,40,70]
 
quick_sort(array, 0, len(array) - 1)
print(array)
