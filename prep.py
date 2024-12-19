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
