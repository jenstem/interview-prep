# # Circular Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        '''
        Adds a new node to the end of the linked list
        '''
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head


    def prepend(self, data):
        '''
        Adds a new node to the beginning of the linked list
        '''
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def print_list(self):
        '''
        Prints the linked list
        '''
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))


    def is_sorted(self):
        '''
        Checks if the linked list is sorted
        '''
        if self.head is None or self.head.next == self.head:
            return True
        temp = self.head
        while temp.next != self.head:
            if temp.data > temp.next.data:
                return False
            temp = temp.next

        return True


    def insert_into_sorted(self, data):
        '''
        Inserts a new node into the sorted linked list
        '''
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        elif data <= self.head.data:
            self.prepend(data)
        else:
            temp = self.head
            while temp.next != self.head and temp.next.data < data:
                temp = temp.next
                new_node.next = temp.next
                temp.next = new_node



cslinkedlist = CSLinkedList()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.append(50)
cslinkedlist.append(60)
print(cslinkedlist.insert_into_sorted())
print(cslinkedlist)
