class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


    def __str__(self):
        """
        Return a string representation of the node.
        """
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None


    def __iter__(self):
        """
        Iterate through the linked list.
        """
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        values = [str(x.value) for x in self]
        return ' -> '.join(values)


    def __len__(self):
        """
        Return the length of the linked list.
        """
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result


    def add(self, value):
        """
        Return the tail node after adding a new node to the linked list.
        """
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail