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


    def count_nodes(self):
        '''
        Counts the number of nodes in the linked list
        '''
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count


    def delete_node(self, key):
        '''
        Deletes a node from the linked list
        '''
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next


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


    def josephus_circle(self, step):
        '''
        Solves the Josephus problem using the circular linked list
        '''
        temp = self.head

        while self.count_nodes() > 1:
            count = 1
            while count != step:
                temp = temp.next
                count += 1
            print(f"Removed: {temp.data}")
            self.delete_node(temp.data)
            temp = temp.next

        return f"Last person left standing: {temp.data}"





cslinkedlist = CSLinkedList()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.append(50)
cslinkedlist.append(60)
print(cslinkedlist.insert_into_sorted())
print(cslinkedlist)
