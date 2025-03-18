# AVL Trees

import QueueLinkedList as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

    def preOrderTraversal(rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)    

newAVL = AVLNode()
newAVL.preOrderTraversal()        
