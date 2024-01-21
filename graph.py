class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def addedge(self,vertex1,vertex2):
        if vertex1 in self.gdict and  vertex2 in self.gdict:
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False
    def addvertex(self,vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex]=[]
            return True
        return False
    def printgraph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])
    def removeedge(self,vertex1,vertex2):
        if vertex1 in self.gdict and vertex2 in self.gdict:
            self.gdict[vertex2].remove(vertex1)
            self.gdict[vertex1].remove(vertex2)
            return True
        return False
    def removevertex(self,vertex):
        if vertex in self.gdict.keys():
            for other_vertex in self.gdict[vertex]:
                self.gdict[other_vertex].remove(vertex)
            del self.gdict[vertex]
            return True
        return False
customdict={
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','e'],
    'd':['b','e','f'],
    'e':['d','f'],
    'f':['d','e']
}
graph1=graph(customdict)
graph1.addvertex('h')
graph1.addedge('h','a')
graph1.addedge('h','b')
graph1.printgraph()
graph1.removeedge('h','a')
graph1.removevertex('h')
graph1.printgraph()