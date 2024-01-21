import heapq
#class for edges
class Edge:
    def __init__(self,weight,start_vertex,target_vertes):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertes
# class for nodes
class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False #after each iteration we willset it to not visit again
        #previous node that we come to this node
        self.predecessor=None
        #children/neighbour:to which you are going
        self.neighbour=[]
        self.min_distance=float("inf")# initial distance
    def __lt__(self, other_node):
        return self.min_distance<other_node.min_distance
        #to compare minimum distance(compare the nodes)
    def add_edge(self,weight,destination_vertex):
        edge=Edge(weight,self,destination_vertex)
        self.neighbour.append(edge)
class Dijkstra:#min_heap
    def __init__(self):
        self.heap=[]
    def calculate(self,start_vertex):
        start_vertex.min_distance=0
        heapq.heappush(self.heap,start_vertex)
        while self.heap:
            actual_vertex=heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            #pop element with lower distance
            for edge in actual_vertex.neighbors:
                start=edge.start_vertex
                target=edge.target_vertex
                new_distance=start.min_distance+edge.weight
                if new_distance<target.min_distance:
                    target.min_distance=new_distance
                    target.predecessor=start
                    heapq.heappush(self.heap,target)
            actual_vertex.visited=True
    def get_shortest_path(self,vertex):
        print('the shortest path to the vertex is :{vertex.min_distance}')
        actual_vertex=vertex
        while actual_vertex is not None:
            print(actual_vertex.name,end=" ")
            actual_vertex=actual_vertex.predecessor

a=Node('A')
b=Node('B')
print(a>b)
