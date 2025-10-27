import array

class StringHash:
    def __init__(self, size = 11):
        if size < 11:
            size = 11
        self.theHeap = array.array('I', [-1] * size)
        self.primeLookup = [23, 53, 103, 211, 509, 1049, 2027]
        self.count = None
        self.size = size

    def hash(self, value):
        return value % self.size

