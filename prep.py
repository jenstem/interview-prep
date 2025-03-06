# Binary Search Tree

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertNode(rootNode, nodeValue):
        if rootNode.data == None:
            rootNode.data = nodeValue
        elif nodeValue <= rootNode.data:
            if rootNode.leftChild == None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                BSTNode.insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild == None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                BSTNode.insertNode(rootNode.rightChild, nodeValue)
        return "The node has been successfully inserted"     

newBST = BSTNode(None)
print(newBST.insertNode(newBST, 70))
print(newBST.insertNode(newBST, 60))
print(newBST.data)
print(newBST.leftChild.data)
print(newBST.rightChild.data)

