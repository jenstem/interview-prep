# Circular Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        '''
        Turns the value of the node into a string
        '''
        return str(self.value)


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


    def append(self, value):
        '''
        Adds a new node to the end of the linked list
        '''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1


    def prepend(self, value):
        '''
        Adds a new node to the beginning of the linked list
        '''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1


    def insert(self, index, value):
        '''
        Adds a new node at the specified position in the linked list
        '''
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of range")
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1


    def traverse(self):
        '''
        Iterates through the linked list
        '''
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break


    def search(self, target):
        '''
        Search for a specific element in the linked list
        '''
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False


    def get(self, index):
        '''
        Get the value of the node at the specified index
        '''
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current




cslinkedlist = CSLinkedList()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.insert(0, 50)
print(cslinkedlist)
print(cslinkedlist.get(2))