import numpy as np

class Stack:

    def __init__(self):

        self.stack_array = np.empty()    #this is the stack array, start empty and add to it
        self.i = 0               #index
        return

    def push(self, datum):
        self.stack_array = np.insert(self.stack_array, self.i, datum)
        self.i = self.i+1
        return

    def pop(self):
        self.i = self.i-1
        return

    def peak(self):
        return self.stack_array[self.i]

    def size(self):
        return self.i


