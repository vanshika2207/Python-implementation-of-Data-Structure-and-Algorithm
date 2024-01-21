class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def bfs(self,start,end):#a,d
        queue=[]
        queue.append([start])#queue=[[a]]
        print(queue)
        while queue:
            path=queue.pop(0) #[a]
            print('path is',path)
            node=path[-1]#a
            print('node is',node)
            if node==end:
                return path
            for adjacent in self.gdict.get(node,[]):
                #gdict.get('a',[])=b,c
                new_path=list(path)#[a] [a]
                print('newpath ',new_path)
                new_path.append(adjacent)#[a,b] [a,c
                print(new_path)
                queue.append(new_path)#[[a,b]]
                print('q',queue)

customdict = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    'e': ['d', 'f'],
    'f': ['d', 'e']
}
g=graph(customdict)
b=g.bfs('a','d')
print(b)