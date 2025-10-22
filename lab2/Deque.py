import array

class Deque:
    def __init__(self, n = 20):
        self.theArray = array.array('i', [0] * n)
        self.head = 0
        self.tail = 0
        self.size = n

    def addTail(self, val):
        if(self.tail + 1 > self.size and self.head != 0):
            self.tail = 0
        if not(self.tail + 1 == self.head):
            self.theArray[self.tail] = val
            self.tail += 1
        return

    def removeHead(self):
        if(self.head == self.tail):
            raise IndexError("Array is empty in removeHead")
        else:
            tmp = self.theArray[self.head]
            self.head += 1
            return tmp

    def dumpArray(self):
        if (self.tail <  self.head):
            tmp = self.theArray
        else:
            tmp = array.array('i', [0] * self.tail)
            for i in range(0, self.tail):
                tmp[i] = self.theArray[i]
        return str(tmp)

    def isEmpty(self):
        if (self.head == self.tail):
            return True
        else:
            return False

    def resize(self):
        tmp = self.theArray
        self.theArray = array.array('i', [0] * 2 * (self.size))
        count = 0
        if(self.head < self.tail):
            count = self.tail - self.head
            for i in range(0, count):
                self.theArray[i] = tmp[i]
        elif(self.head > self.tail):
            count = self.size - (self.head - self.tail)
            for i in range(0, count):
                self.theArray[i] = tmp[i]
        self.head = 0
        self.tail = count
        return


