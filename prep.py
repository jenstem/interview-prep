# Double Linked List

class Node:
    """
    A class representing a node in a doubly linked list.

    Attributes:
        value: The data stored in the node.
        next: A pointer to the next node in the list.
        prev: A pointer to the previous node in the list.
    """
    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Args:
            value: The data to be stored in the node.
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


class DoublyLinkedList:
    """
    A class to represent a Double Linked List.

    Attributes:
        head: The first node in the list.
        tail: The last node in the list.
        length: The number of nodes in the list.
    """
    def __init__(self):
        """
        Initializes an empty Doubly Linked List.
        Sets head and tail to None and length to 0.
        """
        self.head = None
        self.tail = None
        self.length = 0


    def __str__(self):
        """
        Returns a string representation of the double linked list.

        The format is 'value1 <-> value2 <-> value3 <-> ...'

        Returns:
            A string representing the values in the list.
        """
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result


    def append(self, value):
        """
        Creates a new node with the given value and appends it to the end of the list.

        Args:
            value: The data to be stored in the new node.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1


    def prepend(self, value):
        """
        Inserts a new node with the specified value at the beginning of the list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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


    def reverse_traverse(self):
        """
        Prints the values of the nodes in the list in reverse order.
        """
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev


    def search(self, target):
        """
        Searches for a node with the specified value in the list.

        Args:
            target: The value to search for.

        Returns:
            The node containing the target value, or False if the value is not found.
        """
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1


    def get(self, index):
        """
        Deletes the first node found with the specified value from the list.

        Args:
            target: The value to search for and delete.
        """
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node


    def set_value(self, index, value):
        """
        Updates the value of the node at the specified index.

        Args:
            index: The index of the node to update.
            value: The new value to store in the node.
        """
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False


    def insert(self, index, value):
        """
        Inserts a new node with the specified value at the specified index.

        Args:
            index: The index at which to insert the new node.
            value: The value to store in the new node.
        """
        if index < 0 or index > self.length:
            print("Index out of range.")
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node


    def pop_first(self):
        """
        Removes the first node from the list and returns its value.
        """
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node


    def pop(self):
        """
        Removes the last node from the list and returns its value.
        """
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node









newDLL = DoublyLinkedList()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
newDLL.prepend(50)
print(newDLL.pop())
print(newDLL)