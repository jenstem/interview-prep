# Circular Doubly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


    def __str__(self):
        return str(self.value)


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


new_cdll = CircularDoublyLinkedList()
print(new_cdll)