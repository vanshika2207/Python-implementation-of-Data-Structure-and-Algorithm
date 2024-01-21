import QueueLinkedList as queue
class BSTNode:
    def __init__(self,data):
        self.data=data
        self.rightchild=None
        self.leftchild=None
def insert(rootnode,nodevalue):
    if rootnode.data==None:
        rootnode.data=nodevalue
    elif nodevalue<=rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild=BSTNode(nodevalue)
        else:
            insert(rootnode.leftchild,nodevalue)
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild=BSTNode(nodevalue)
        else:
            insert(rootnode.rightchild,nodevalue)
        return 'success'
bst=BSTNode(None)
insert(bst,70)
insert(bst,60)
insert(bst,80)
print(bst.data)
print(bst.rightchild.data)
print(bst.leftchild.data)
print()
def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)
preorder(bst)
def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)
print()
inorder(bst)
print()
def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)
postorder(bst)
print()

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            root=customqueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild is not  None):
                customqueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customqueue.enqueue(root.value.rightchild)
levelorder(bst)
def search(root_node, node_value):
    if root_node.data == node_value:
        print("The element has been found.")
    elif node_value < root_node.data:
        if root_node.leftchild.data == node_value:
            print("The element has been found.")
        else:
            search(root_node.leftchild, node_value)
    else:
        if root_node.rightchild.data == node_value:
            print("The element has been found.")
        else:
            search(root_node.rightchild, node_value)


print()
search(bst,80)
def minvalue(bstnode):
    current=bstnode
    while current.leftchild is not  None:
        current=current.leftchild
    return current
def delete(rootnode,node):
    if rootnode is None:
        return rootnode
    if node<rootnode.data:
        rootnode.leftchild=delete(rootnode.leftchild,node)
    elif node>rootnode.data:
        rootnode.rightchild=delete(rootnode.rightchild,node)
    else:
        if rootnode.leftchild is None:
            temp=rootnode.rightchild
            rootnode=None
            return temp
        if rootnode.rightchild is None:
            temp=rootnode.leftchild
            rootnode=None
            return temp
        temp=minvalue(rootnode.rightchild)
        rootnode.data=temp.data
        rootnode.rightchild=delete(rootnode.rightchild,temp.data)
    return rootnode
delete(bst,70)
preorder(bst)