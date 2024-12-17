# Create a Stack with a List
# No size limit

class Stack:
    """
    A class to represent a Stack data structure.
    """
    def __init__(self):
        """
        Initialize the stack with an empty list.
        """
        self.list = []

    def __str__(self):
        """
        Return a string representation of the stack.
        """
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        """
        Check if the stack is empty.
        """
        return len(self.list) == 0

    def push(self, value):
        """
        Add an element to the top of the stack.
        """
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        """
        Remove and return the top element of the stack.
        """
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        """
        Return the top element of the stack without removing it.
        """
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        """
        Delete the stack.
        """
        self.list = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.delete())