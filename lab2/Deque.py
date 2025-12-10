import array

class Deque:
    def __init__(self, n = 20):
        self.theArray = array.array('i', [0] * n)
        self.head = -1
        self.tail = 1
        self.size = n
        self.count = 0
        self.stupidassneg = 0

    def addTail(self, val):
        if self.count == self.size:
            self. theArray = self.resize()
            self.addTail(val)
            return
        elif self.tail - 1 == self.size:
            self.tail = 1
            self.theArray[self.tail - 1] = val
            self.count += 1
            self.tail += 1
        else:
            self.theArray[self.tail - 1] = val
            self.count += 1
            self.tail += 1
            return

    def removeHead(self):
        if self.count == 0:
            raise IndexError("Array is empty in removeHead")
        if self.head + 1 == self.size:
            tmp = self.theArray[-(self.size)]
            self.head = -(self.size)
            self.count -= 1
            return tmp
        else:
            tmp = self.theArray[self.head + 1]
            self.head += 1
            self.count -= 1
            return tmp

    def dumpArray(self):
        tmp = ""
        for i in range(0, self.count):
            tmp += str(self.theArray[i]) + " "
        return tmp
    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def resize(self):
        tmp = array.array('i', [0] * self.size * 2)
        tmp2 = self.count
        for i in range(0, tmp2):
            if not(self.size - 1 == self.head):
                tmp[i] = self.theArray[self.head + 1]
                self.head += 1
            elif self.size -1 == self.head:
                self.head = -1
                tmp[i] = self.theArray[self.head + 1]
                self.head += 1
        self.head = -1
        self.size = self.size * 2
        self.tail = self.count + 1
        return tmp

    def listQueue(self):
        tmp1 = self.head
        tmp2 = self.tail
        tmpO = ""

        for i in range(0, self.count):
            if not(self.size - 1 == tmp1):
                tmpO += str(self.theArray[tmp1 + 1]) + " "
                tmp1 += 1
            elif self.size -1 == tmp1:
                tmp1 = -1
                tmpO += str(self.theArray[tmp1 + 1]) + " "
                tmp1 += 1
        return tmpO

    def addHead(self, val):
        if self.size == abs(self.head):
            self.head = 0
        if self.size  == self.count:
            self.theArray = self.resize()
            self.addHead(val)
        elif not(self.size == self.head - 1):
            self.theArray[self.head] = val
            self.head -= 1
            self.count += 1
        else:
            self.head -= 1
            self.theArray[self.head] = val
            self.count += 1
        return

    def removeTail(self):
        if self.count == 0:
            raise IndexError("Array is empty in removeTail")
        else:
            tmp = self.theArray[self.tail - 2]
            self.tail -= 1
            self.count -= 1
            return tmp

    def negResize(self):
        tmp = array.array('i', [0] * self.size * 2)
        for i in range(0, self.count):
            if(self.head + 1 == self.size):
                tmp[i]=self.theArray[-(self.size)]
                self.head = -(self.size)
            else:
                tmp[i]  = self.theArray[self.head + i]
        self.head = -1
        self.tail = self.count + 1
        self.size = self.size * 2
        self.stupidassneg = 0
        return tmp

    def solveThink(self, inArray, number):
        for i in reversed(range(number)):
            self.addTail(inArray[i])




