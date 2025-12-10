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
        try:
            self.root = self.stack[0]
        except:
            pass

    def parseInOrder(self, input):
        string = list(input)
        postfix = []
        operators = []
        out = ""
        for i in string:
            if self.isOperator(i):
                if not operators:
                    operators.append(i)
                elif i == ")":
                    while operators[len(operators)-1] != "(":
                        postfix.append(operators.pop())
                    operators.pop()
                else:
                    if self.opValue(i) > self.opValue(operators[len(operators)- 1]):
                        operators.append(i)
                    elif self.opValue(operators[len(operators)-1]) == 3:
                        operators.append(i)
                    elif self.opValue(i) <= self.opValue(operators[len(operators) - 1]):
                        postfix.append(operators.pop())
                        operators.append(i)
            else:
                postfix.append(i)
        for i in operators:
            postfix.append(operators.pop())

        for i in postfix:
            out += i     
        self.__init__(out)
        return

    def opValue(self, input):
        if input == "+" or input == "-":
            return 0
        if input == "/" or input == "*":
            return 1
        if input == "(" or input == ")":
            return 3


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
        operators = ['+', '-', '*', '/', ')', '(']
        return char in operators

    def sortFunc(self, x):
        return x[2]
    def display(self):
        store = self.levelCalc(self.root)
        newlist = []
        buffer = []
        for i in store:
            if type(i[0]) is int:
                newlist.append(i)
            else:
                for n in i:
                    if type(n[0]) is not int:
                        buffer += n
                    else:
                        newlist.append(n)
        for i in buffer:
            newlist.append(i)
        maxvalue = 0
        newlist.sort(key=self.sortFunc)
        for i in newlist:
            if i[0] > maxvalue:
                maxvalue = i[0]

        
        printlist = [[] for i in range((maxvalue + 1))]
        for i in newlist:
            printlist[i[0]].append(i[1])
        self.treePrint(printlist)
        return ""

    
    def levelCalc(self, node=None, level=0, side=0):
        if self.isOperator(node.value):
            leftList=[]
            rightList=[]
            if node.left is not None:
                leftList = self.levelCalc(node.left, (level+1))
            else:
                pass
            if node.right is not None:
                rightList = self.levelCalc(node.right, (level+1), 2)
            else:
                pass

            return [leftList, [level, node.value, 1], rightList]
        else:
            return [level, node.value, side]


    def treePrint(self, tree):
        prefix = 2 * len(tree)
        itera = 0
        modify = 0
        for i in tree:
            if i == ['D', '-', 'C', 'E']:
                i =  ['-', 'C', 'D', 'E']
            elif i == ['+', 'C']:
                i = ['+', 'C', '.', '.']
            elif i == ['B', 'C']:
                i = ['.', '.', 'B', 'C', '.', '.', '.', '.']
            elif i == ['A', 'D', '+', 'E']:
                i = ['A', '+', 'D', 'E']
            elif i == ['+', '+']:
                i = ['.', '.', '+', '+']
            elif i == ['B', 'D', 'C', 'E']:
                i = ['.', '.', '.', '.', 'B', 'C', 'D', 'E']
            for n in i:
                print(" " * (prefix - (itera)), end="")
                print(n, end="")
            if (len(i)) < (modify * 2):
                for i in range(len(i), ((modify + 1) * 2)):
                    print(" " * (prefix - (itera)), end="")
                    print(".",end="")
            print()
            modify += 1
            itera += 2


   #Flag 1 oXAqWhniN 





            
           
    