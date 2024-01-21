class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def addedge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False
    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            devertex=queue.pop(0)
            print(devertex)
            for adjvertex in self.gdict[devertex]:
                if adjvertex not in visited:
                    visited.append(adjvertex)
                    queue.append(adjvertex)
    def dfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popvertex=stack.pop()
            print(popvertex)
            for adjvertex in self.gdict[popvertex]:
                if adjvertex not in visited:
                    visited.append(adjvertex)
                    stack.append(adjvertex)
customdict={
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','e'],
    'd':['b','e','f'],
    'e':['d','f'],
    'f':['d','e']
}
g=Graph(customdict)
g.addedge('a','e')
print(g.gdict)
g.bfs('a')
g.dfs('a')