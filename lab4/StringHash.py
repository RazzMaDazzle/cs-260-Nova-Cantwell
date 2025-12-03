import math

class StringHash:
    def __init__(self, size = 11):
        if size < 11:
            size = 11
        self.theHeap = ["_empty_" for i in range(size)]
        self.primeLookup = [23, 53, 103, 211, 509, 1049, 2027]
        self.count = 0
        self.size = size

    def hashFunc(self, key):
        hashValue = 0

        for c in range(len(key)):
            hashValue *= 128
            hashValue += ord(key[c])
            hashValue %= self.size

        return hashValue

    def primeGen(self):
        size = self.size * 2
        x = True

        while x:
            np = False
            for i in range(2, size):
                if  size % i == 0:
                    np = True
            if np == False:
                x = False
                self.size = size
            else:
                size += 1
        return

    def resize(self):
        tmp = ["_empty_" for i in range(self.size)]
        for x in range(0, len(self.theHeap)):
            if self.theHeap[x] != "_empty":
                position = self.hashFunc(self.theHeap[x])
                updated = False
                for i in range(0, self.size - position):
                    if tmp[position + i] == "_empty_" and not updated:
                        tmp[position + i] = self.theHeap[x]
                        updated = True
                        self.count += 1
                if not updated:
                    for i in range(0, position):
                        if tmp[i] == "_empty_" and not updated:
                            tmp[i] =  self.theHeap[x]
                            updated = True
                            self.count += 1
        self.theHeap = tmp
        return

    def addItem(self, item):
        if  (self.size + 1) / (self.count + 1) == 2:
            self.primeGen()
            self.resize()
        position = self.hashFunc(item)
        updated = False
        for i in range(0, self.size - position):
            if self.theHeap[position + i] == "_empty_" and not updated:
                self.theHeap[position + i] = item
                updated = True
                self.count += 1
        if not updated:
            for i in range(0, position):
                if self.theHeap[i] == "_empty_" and not updated:
                    self.theHeap[i] = item
                    updated = True
                    self.count += 1
        return

    def findItem(self, item):
        position = self.hashFunc(item)
        found = False

        for i in range(0, self.size - position):
            if self.theHeap[position + i] == item and not found:
                found = True

        if not found:
            for i in range(0, position):
                if self.theHeap[i] == item and not found:
                    found = True
        return found

    def removeItem(self, item):
        position = self.hashFunc(item)
        deleted = False

        for i in range(0, self.size - position):
            if self.theHeap[position + i] == item and not deleted:
                self.theHeap[position + i] = "_deleted_"
                deleted = True

        if not deleted:
            for i in range(0, position):
                if self.theHeap[i] == item and not deleted:
                    self.theHeap[i] = "_deleted_"
                    deleted = True
        return

    def displayTable(self):
        string = ""
        for i in range(0, len(self.theHeap)):
            string = string + (self.theHeap[i] + "\n")
        return string