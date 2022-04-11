import heapq
#input
files=[5,7,3,10,1,5]
#minimum of operation
print(files)
heap_files=list(files)
heapq.heapify(heap_files)
total_operation=0
while (len(heap_files)>1):
    fileA=heapq.heappop(heap_files)
    fileB=heapq.heappop(heap_files)
    fileC=fileA+fileB
    total_operation=total_operation+fileC
    heapq.heappush(heap_files, fileC)

print(total_operation)
