# Create a Stack with a List
# No size limit


class Stack:
    def __init__(self):
        self.list = []


    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
