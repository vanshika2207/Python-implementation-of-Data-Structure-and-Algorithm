class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
    def __str__(self,level=0):
        ret="  "*level+str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

    def addchild(self,treenode):
        self.children.append(treenode)

tree=TreeNode('Drinks',[])
cold=TreeNode('cold',[])
hot=TreeNode('hot',[])
tree.addchild(cold)
tree.addchild(hot)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addchild(cola)
cold.addchild(fanta)
hot.addchild(tea)
hot.addchild(coffee)

print(tree)