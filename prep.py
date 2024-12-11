from random import randint


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


    def generate(self, n, min_value, max_value):
        """
        Generate a linked list from a list of values.
        """
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


    def remove_duplicates(ll):
        if ll.head is None:
            return

        current_node = ll.head
        prev_node = None

        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            prev_node = current_node
            current_node = current_node.next
        ll.tail = prev_node
        return ll.head


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(len(customLL))