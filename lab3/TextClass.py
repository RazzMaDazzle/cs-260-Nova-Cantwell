class TextClass:
    def __init__(self):
        self.node = None
        self.next = None
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

    def traverseHead(self, node):
        if(node.prev == None):
            return node
        else:
            return self.traverseHead(node.prev)

    def traverseTail(self, node):
        if node.next is None:
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

    def findNode(self, value, node):
        tmp = self.traverseHead(node)
        while(tmp != None):
            if tmp.value == value:
                if (self.next is None or self.next is not tmp):
                    self.next = tmp
                    return tmp
                else:
                    pass
            tmp = tmp.next
        return False

    def findNext(self, value):
        tmp = self.findNode(value, self.node)
        if tmp:
            return True
        else:
            return False

    def find(self, value):
        if(self.node == None):
            raise ValueError("Empty List")
        else:
            tmp = self.findNode(value, self.node)
            if tmp:
                return True
            else:
                return False

    def findRemove(self, value):
        if(self.node == None):
            raise ValueError("Empty List")
        else:
            tmp = self.findNode(value, self.node)
            if tmp:
                if(tmp == self.node):
                    if(tmp.prev != None):
                        tmp.prev.next = tmp.next
                        self.node = tmp.prev
                    elif(tmp.next != None):
                        tmp.next.prev = tmp.prev
                        self.node = tmp.next
                    else:
                        self.node = None
                else:
                    if(tmp.prev != None):
                        tmp.prev.next = tmp.next
                        tmp = tmp.prev
                    else:
                        tmp.next.prev = tmp.prev
                        tmp = tmp.next
                return True
            else:
                return False

    def append(self, tclass):
        tmp = tclass.traverseHead(tclass.node)
        tmp2 = self.traverseTail(self.node)

        tmp2.next = tmp
        tmp.prev = tmp2
        return

    def removeLast(self, node=None):
        if self.next is not None:
            if node is None:
                node = self.traverseHead(self.node)
            if self.next is self.node:
                if self.node.next is not None:
                    self.node.next.prev = self.node.prev
                    self.node = self.next
                elif self.node.prev is not None:
                    self.node.prev.next = self.next
                    self.node = self.node.prev
                else:
                    self.node = None
            else:
                if node is self.next:
                    node.next.prev = node.prev
                    if node.prev is not None:
                        node.prev.next = node.next
                        node = None
                elif node.next is not None:
                    return self.removeLast(node.next)
                else:
                    return
        else:
            return

    def insertLast(self, value, node=None):
        if self.next is not None:
            tmp = Node(value)
            if node is None:
                node = self.traverseHead(self.next)
            if self.node is self.next:
                tmp.prev = self.node.prev
                tmp.next = self.node
                self.node.prev.next = tmp
                self.node.prev = tmp
            elif node is self.next:
                tmp.prev = node.prev
                tmp.next = node
                node.prev.next = tmp
                node.prev = tmp
            else:
                if node.next is not None:
                    self.insertLast(value, node.next)
                else:
                    return
        else:
            return

    def thinkSolve(self, tclass):
        self.append(tclass)
        return
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None