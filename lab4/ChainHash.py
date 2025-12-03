class ChainHash:
    def __init__(self, size = 7):
        if size < 7:
            size = 7
        self.theHeap = ["_empty_" for i in range(size)]
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
        self.primeGen()
        tmp = ["_empty_" for i in range(self.size)]
        for i in range(0, len(self.theHeap)):
            if self.theHeap[i] == "_empty_":
                pass
            else:
                for n in reversed(range(0, len(self.theHeap[i]))):
                    position = self.hashFunc(self.theHeap[i][n])
                    if tmp[position] == "_empty_":
                        tmp[position] = [self.theHeap[i][n]]
                    else:
                        tmp[position].append(self.theHeap[i][n])
        self.theHeap = tmp
        return

    def addItem(self, item):
        position = self.hashFunc(item)
        if self.theHeap[position] == "_empty_":
            self.theHeap[position] = [item]
            self.count += 1
        else:
            self.theHeap[position].append(item)
            self.count += 1
        if (self.count + 2) > (self.size * 2):
            self.resize()
        return

    def findItem(self, item):
        position = self.hashFunc(item)
        found = False
        if self.theHeap[position] == "_empty_":
            pass
        else:
            for i in range(0, len(self.theHeap[position])):
                if self.theHeap[position][i] == item:
                    found = True
                else:
                    pass
        return found

    def removeItem(self, item):
        position = self.hashFunc(item)
        deleted = False
        if self.theHeap[position] == "_empty_":
            pass
        else:
            for i in range(0, len(self.theHeap[position])):
                if self.theHeap[position][i] == item:
                    self.theHeap[position].pop(i)
                    if i == 0:
                        self.theHeap[position] = "_empty_"
                else:
                    pass
        return

    def displayTable(self):
        string = ""
        for i in range(0, len(self.theHeap)):
            if self.theHeap[i] == "_empty_":
                string = string + (self.theHeap[i] + "\n")
            else:
                for n in range(0, len(self.theHeap[i])):
                    string = string + (self.theHeap[i][n] + " ")
                string = string + "\n"
        return string
