from collections import defaultdict
class graph:
    def __init__(self,numberofvertices):
        self.graph=defaultdict(list)
        self.numberofvertices=numberofvertices
    def addedge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def topologicalhelper(self,v,visited,stack):#v-vertex
        visited.append(v) #v=a ,visited=[a],[a,b],[a,b,c]
        for i in self.graph[v]:#[b],[c]
            if i not in visited:
                self.topologicalhelper(i,visited,stack)
                #(b,[a],[]),(c,[a,b],[])
        stack.insert(0,v)  #c,b,a
    def topologicalsort(self):
        visited=[]
        stack=[]
        for k in list(self.graph):
            if k not in visited:
                self.topologicalhelper(k,visited,stack)
        print(stack)

#a->b->c
customgraph=graph(4)
customgraph.addedge('a','b')
customgraph.addedge('b','c')
customgraph.topologicalsort()