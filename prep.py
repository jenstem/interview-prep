# Stack and Queue Interview Questions

# Three in One

# Describe how you could use a single Python list to implement three stacks.

# Can divide a list into 3 equal parts and use each part as a stack.

# [0,1,2,3,4,5,6,7,8]

# Stack 1 - [0 to n/3) - goes from 0 to n/3 or 2
# Stack 2 - [n/3 to 2n/3) - goes from n/3 or 3 to 2n/3 or 5
# Stack 3 - [2n/3 to n) - goes from 2n/3 or 6 to n or 8

class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.custList = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "Stack is full"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "Stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "Stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value


customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.pop(0))