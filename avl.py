import QueueLinkedList as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

newTree = AVLNode(10)
def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftChild)
    print(rootnode.data)
    inorder(rootnode.rightChild)
def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot
def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot
# Implementing Insertion in an AVL Tree
def getHeight(root_node):
    if not root_node:
        return 0
    return root_node.height


def getBalance(root_node):
    if not root_node:
        return 0
    return getHeight(root_node.leftChild) - getHeight(root_node.rightChild)


def insertNode(root_node, node_value):
    if not root_node:
        return AVLNode(node_value)
    elif node_value < root_node.data:
        root_node.leftChild = insertNode(root_node.leftChild, node_value)
    else:
        root_node.rightChild = insertNode(root_node.rightChild, node_value)

    root_node.height = 1 + max(getHeight(root_node.leftChild), getHeight(root_node.rightChild))
    balance = getBalance(root_node)
    if balance > 1 and node_value < root_node.leftChild.data:
        return rightRotate(root_node)
    if balance > 1 and node_value > root_node.leftChild.data:
        root_node.leftChild = leftRotate(root_node.leftChild)
        return rightRotate(root_node)
    if balance < -1 and node_value > root_node.rightChild.data:
        return leftRotate(root_node)
    if balance < -1 and node_value < root_node.rightChild.data:
        root_node.rightChild = rightRotate(root_node.rightChild)
        return leftRotate(root_node)
    return root_node

def getminvalue(rootnode):
    if rootnode is None or rootnode.leftChild is None:
        return rootnode
    return getminvalue(rootnode.leftChild)
def deletenode(rootnode,nodevalue):
    if not rootnode:
        return rootnode
    elif nodevalue<rootnode.data:
        rootnode.leftChild=deletenode(rootnode.leftChild,nodevalue)
    elif nodevalue>rootnode.data:
        rootnode.rightChild=deletenode(rootnode.rightChild,nodevalue)
    else:
        if rootnode.leftChild is None:
            temp=rootnode.rightChild
            rootnode=None
            return temp
        elif rootnode.rightChild is None:
            temp=rootnode.leftChild
            rootnode=None
            return temp
        temp=getminvalue(rootnode.rightChild)
        rootnode.data=temp.data
        rootnode.rightChild=deletenode(rootnode.rightChild,temp.data)
    balance=1+max(getBalance(rootnode.leftChild),getBalance(rootnode.rightChild))
    if balance>1 and getBalance(rootnode.leftChild)>=0:
        return rightRotate(rootnode)
    if balance>1 and getBalance(rootnode.leftChild)<0:
        rootnode.leftChild=leftRotate(rootnode.leftChild)
        return rightRotate(rootnode)
    if balance<-1 and getBalance(rootnode.rightChild)<=0:
        return leftRotate(rootnode)
    if balance<-1 and getBalance(rootnode.rightChild)>0:
        rootnode.rightChild=rightRotate(rootnode.rightChild)
        return leftRotate(rootnode)
    return rootnode
# Initializing the AVL Tree
def deleteentire(rootnode):
    rootnode.data=None
    rootnode.leftChild=None
    rootnode.rightChild=None

newTree = AVLNode(70)
newTree = insertNode(newTree, 50)
newTree = insertNode(newTree, 90)
newTree = insertNode(newTree, 30)
newTree = insertNode(newTree, 80)
newTree = insertNode(newTree, 100)
newTree = insertNode(newTree, 20)
newTree = insertNode(newTree, 40)
inorder(newTree)
print()
deletenode(newTree,50)
inorder(newTree)
print()
deleteentire(newTree)
inorder(newTree)