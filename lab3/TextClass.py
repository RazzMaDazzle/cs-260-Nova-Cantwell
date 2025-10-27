class TextClass:
    def __init__(self):
        self.node = None
        pass

    def addHead(self, value):
        if(self.node == None):
            self.node = Node(value)
            return
        else:
            tmp = self.traverseHead(self.node)
            tmp.prev = Node(value)
            tmp.prev.next = tmp
            return

    def addTail(self, value):
        if(self.node == None):
            self.node = Node(value)
            return
        else:
            tmp = self.traverseTail(self.node)
            tmp.next = Node(value)
            tmp.next.prev = tmp
            return

    def getHead(self):
        if(self.node == None):
            raise ValueError("Empty List")
        else:
            tmp = self.traverseHead(self.node)
        return tmp.value

    def getTail(self):
        if(self.node == None):
            raise ValueError("Empty List")
        else:
            tmp = self.traverseTail(self.node)
        return tmp.value

    def traverseHead(self, node, value=None):
        if(node.prev == None):
            return node
        elif(value != None):
            if(value == node.value):
                return node
        else:
            return self.traverseHead(node.prev)

    def traverseTail(self, node):
        if(node.next == None):
            return node
        else:
            return self.traverseTail(node.next)

    def traverseTailf(self, node, value):
        if(value == node.value):
            return node
        else:
            return self.traverseTail(node.next)

    def removeHead(self):
        if(self.node == None):
            raise ValueError("Empty List")
        else:
            tmp = self.traverseHead(self.node)
            if(tmp.next != None):
                if(tmp == self.node):
                    self.node = self.node.next
                    self.node.prev = None
                else:
                    tmp.next.prev = None
                    tmp.node = tmp.next
            else:
                self.node = None
            return

    def removeTail(self):
        if(self.node == None):
            raise ValueError("Empty List")
        else:
            tmp = self.traverseTail(self.node)
            if(tmp.prev != None):
                if(tmp == self.node):
                    self.node = self.node.prev
                    self.node.next = None
                else:
                    tmp.prev.next = None
                    tmp.node = tmp.prev
            else:
                self.node = None
            return

    def displayList(self):
        tmp = self.traverseHead(self.node)
        tstr = ""
        while(tmp.next != None):
            tstr += str(tmp.value) + " "
            tmp = tmp.next
        tstr += str(tmp.value) + " "
        return tstr

    def findNode(self, value):
        if(self.node == None):
            raise ValueError("Empty List")
        else:
            tmp


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None