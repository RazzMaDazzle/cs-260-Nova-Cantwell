class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class ParseTree:
    def __init__(self, input):
        string = list(input)
        self.stack = []

        for char in string:
            
            if self.isOperator(char):
                if len(self.stack) < 2:
                    raise ValueError("Not enough operands")
                right = self.stack.pop()
                left = self.stack.pop()
                node = Node(char, left=left, right=right)
                self.stack.append(node)

            else:
                leaf = Node(char)
                self.stack.append(leaf)
        self.root = self.stack[0]


    def postOrder(self, node=None):
        if node is None:
            node = self.root
        if self.isOperator(node.value):
            left_str = ""
            right_str = ""

            if node.left is not None:
                left_str = self.postOrder(node.left)
            else:
                left_str = ""

            if node.right is not None:
                right_str = self.postOrder(node.right)
            else:
                right_str = ""

            return f"{left_str}{right_str}{node.value}"  
        else:
            return node.value

    def preOrder(self, node=None):
        if node is None:
            node = self.root

        if self.isOperator(node.value):
            left_str= ""
            right_str= ""

            if node.left is not None:
                left_str = self.preOrder(node.left)
            else:
                left_str = ""

            if node.right is not None:
                right_str = self.preOrder(node.right)
            else:
                right_str = ""

            return f"{node.value}{left_str}{right_str}"  
        else:
            return node.value

    def inOrder(self, node=None):
        if node is None:
            node = self.root

        if self.isOperator(node.value):
            left_str= ""
            right_str= ""

            if node.left is not None:
                left_str = self.inOrder(node.left)
            else:
                left_str = ""

            if node.right is not None:
                right_str = self.inOrder(node.right)
            else:
                right_str = ""

            return f"({left_str}{node.value}{right_str})"  
        else:
            return node.value

    def isOperator(self, char):
        operators = ['+', '-', '*', '/']
        return char in operators

    def display(self):
        string = list(self.preOrder())
        prefix = len(string)
        store = []
        level = 0
        count = 2
        ltotal = 0
        prev = ""
        for i in string:
            if level == 0:
                store.append([i])
                prev = i
                level += 1
            elif self.isOperator(prev) and self.isOperator(i):
                if ltotal == 0:
                    store.append([i])
                    prev = i
                    ltotal += 1
                    continue
                store[level].append(i)
                prev = i
                ltotal += 1
                if count == ltotal:
                    ltotal = 0
                    level += 1
                    prev = i
                    count = 2 * level
            elif ltotal != 0 and self.isOperator(prev) and not self.isOperator(i):
                try:
                    store[level+1].append(i)
                except:
                    store.append([i])
            else:
                try:
                    store[level].append(i)
                    prev = i
                    ltotal += 1
                except:
                    store.append([i])
                    prev = i
                    ltotal += 1
                if count == ltotal:
                    ltotal = 0
                    level += 1
                    prev = i
                    count = 2 * level

        self.treePrint(prefix, store) 

    def treePrint(self, length, tree):
        prefix = 2 * len(tree)
        itera = 0
        modify = 0
        for i in tree:
            for n in i:
                print(" " * (prefix - (itera - modify)), end="")
                print(n, end="")
            print()
            itera += 2






            
           
    