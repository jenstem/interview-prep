# Stack and Queue Interview Questions

# Queue via Stacks

# Implement a Queue class which implements a queue using two stacks.

class Stack():
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)