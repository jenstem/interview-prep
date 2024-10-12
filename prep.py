# Circular Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def __str__(self):
        '''
        Converts an instance of class into a string
        '''
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        return result


cslinkedlist = CSLinkedList()
print(cslinkedlist)