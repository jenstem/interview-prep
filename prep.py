# Circular Doubly Linked List

class Node:
    """
    A class to represent a node in a Circular Doubly Linked List.
    """
    def __init__(self, value):
        """
        Initialize the node with a value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None
        self.prev = None


    def __str__(self):
        """
        Returns a string representation of the node, showing its value
        and references to the previous and next nodes.

        Returns:
            A formatted string representing the node.
        """
        return str(self.value)


class CircularDoublyLinkedList:
    """
    A class to represent a Circular Doubly Linked List.
    """
    def __init__(self):
        """
        Initialize the Circular Doubly Linked List.
        Sets head and tail to None and length to 0.
        """
        self.head = None
        self.tail = None
        self.length = 0


    def __str__(self):
        """
        Returns a string representation of the node, showing its value
        and references to the previous and next nodes.

        The format is 'value1 <-> value2 <-> value3 <-> ...'

        Returns:
            str: The string representation of the node.
        """
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head: break
            result += ' <-> '
        return result


    def append(self, value):
        """
        Creates a new node with the given value and appends it to the end of the list.

        Args:
            value: The value to be stored in the new node.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1


    def prepend(self, value):
        """
        Inserts a new node with the specified value at the beginning of the list.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def traverse(self):
        """
        Prints the values of the nodes in the list.
        """
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break


    def reverse_traverse(self):
        """
        Prints the values of the nodes in the list in reverse order.
        """
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break


    def search(self, target):
        """
        Searches for a node with the given value in the list.
        """
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False


    def get(self, index):
        """
        Retrieves the node at the specified index in the list.
        """
        if index < 0 or index >= self.length:
            return None
        current_node = None
        if index < self.length // 2:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for i in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node




new_cdll = CircularDoublyLinkedList()
new_cdll.append(10)
new_cdll.append(20)
new_cdll.append(30)
new_cdll.append(40)
new_cdll.append(50)
print(new_cdll.get(9))
print(new_cdll)
