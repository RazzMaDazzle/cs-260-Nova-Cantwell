import array

class Deque:
    def __init__(self, n = 20):
        self.theArray = array.array('i', [0] * n)
        self.head = -1
        self.tail = 1
        self.size = n
        self.count = 0

    def addTail(self, val):
        print("dcall")
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
            print(val)
            print(self.theArray[self.tail - 1])
            self.count += 1
            self.tail += 1
            print(self.theArray)
            print(self.head)
            print(self.tail)
            return

    def removeHead(self):
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
        print("call")
        print(self.count)
        print("####")
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
        print(tmp)
        print(self.tail)
        self.head = -1
        self.size = self.size * 2
        self.tail = self.count + 1
        return tmp



