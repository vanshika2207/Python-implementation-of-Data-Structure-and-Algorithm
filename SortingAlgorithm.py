
l = [14,2,56,78,245,6779,44,11, 1, 21, 31, 12]


def bubblesort(n):
    for i in range(len(n) - 1):
        for j in range(len(n) - i - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return (n)


a = bubblesort(l)
print('bubblesort', a)


def selectionsort(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i + 1, len(n)):
            if n[min_index] > n[j]:
                n[min_index], n[j] = n[j], n[min_index]
    return (n)


a = selectionsort(l)
print('selectionsort', a)


def insertionsort(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        while j <= 0 and key < n[j]:
            n[j + 1] = n[j]
            j = j - 1
        n[j + 1] = key
    return (n)


a = insertionsort(l)
print('insertionsort', a)
import math


def bucketsort(n):
    numberofbuckets = round(math.sqrt(len(n)))
    maxvalue = max(n)
    arr = []
    for i in range(numberofbuckets):  # [[][][]]
        arr.append([])
    for j in n:
        index_b = math.ceil(j * numberofbuckets / maxvalue)
        arr[index_b - 1].append(j)
    for i in range(numberofbuckets):
        arr[i] = insertionsort(arr[i])
    k = 0
    for i in range(numberofbuckets):
        for j in range(len(arr[i])):
            n[k] = arr[i][j]
            k += 1
    return n


a = bucketsort(l)
print('bucketsort', a)


def merge(n, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = n[l + i]
    for j in range(0, n2):
        R[j] = n[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            n[k] = L[i]
            i += 1
        else:
            n[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        n[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        n[k] = R[j]
        j += 1
        k += 1


def mergesort(n, l, r):
    if l < r:
        m = (l + (r - 1))
        mergesort(n, l, m)
        mergesort(n, m + 1, r)
        merge(n, l, m, r)
    return (n)


a = mergesort(l, 0, len(l) - 1)
print('mergesort', a)


def pivot(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quicksort(array, start, end):
    if start >= end:
        return
    p = pivot(array, start, end)
    quicksort(array, start, p - 1)
    quicksort(array, p + 1, end)
    return array


a = quicksort(l, 0, len(l) - 1)
print('quick sort', a)

def heapify(customlist,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and customlist[l]<customlist[smallest]:
        smallest=l
    if r < n and customlist[r] < customlist[smallest]:
        smallest = r
    if smallest!=i:
        customlist[i],customlist[smallest]=customlist[smallest],customlist[i]
        heapify(customlist,n,smallest)
def heapsort(customlist):
    n=len(customlist)
    for i in range(int(n/2)-1,-1,-1):
        heapify(customlist,n,i)
    for i in range(n-1,0,-1):
        customlist[i], customlist[0] = customlist[0], customlist[i]
        heapify(customlist,i,0)
    customlist.reverse()
    return customlist
a=heapsort(l)
print('heapsort',a)

def countingSort(arr):
    count=[0]*(max(arr)+1)
    for num in arr:
        count[num]+=1
    sortarr=[]
    for i in range(len(count)):
        while count[i]!=0:
            count[i]-=1
            sortarr.append(i)
    return sortarr
a=countingSort(l)
print('count sort',a)