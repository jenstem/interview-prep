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




new_node = Node(10)
print(new_node.value)