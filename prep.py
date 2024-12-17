# Create a Stack with a List
# No size limit

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[len(self.list)-1]




customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())