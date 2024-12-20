# Create a Stack with a List
# With size limit

class Stack:
    """
    A class to represent a Stack data structure.
    """
    def __init__(self, maxSize):
        """
        Initialize the stack with an empty list.
        """
        self.maxSize = maxSize
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

    def isFull(self):
        """
        Check if the stack is full.
        """
        return len(self.list) == self.maxSize

    def push(self, value):
        """
        Add a value to the stack.
        """
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully added to the stack"