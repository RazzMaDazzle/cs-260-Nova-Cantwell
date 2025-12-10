class Node:
    def __init__(self, value):
        self.deleted = False
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None

    def insertValue(self, value, node = None):
        if self.root is None:
            self.root = Node(value)
        if node is None:
            node = self.root
        if node.value == value and node.deleted:
            node.deleted = False
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insertValue(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insertValue(value, node.right)

    
    def removeValue(self, value):
        return self.findValue(value, self.root, True)
    def findValue(self, value, node=None, setD = False):
        if not self.root:
            raise IndexError("Empty Tree")
            return
        if node is None:
            node = self.root
        if node.left is not None or node.right is not None:
            if node.value == value:
                if setD:
                    node.deleted = True
                    return True
                if not node.deleted:
                    return True
                else:
                    return False
            else:
                if node.left is not None:
                    result = self.findValue(value, node.left, setD)
                    if result:
                        return result
                if node.right is not None:
                    result = self.findValue(value, node.right, setD)
                    if result:
                        return result
                return result
                
        else:
            if node.value == value:
                if setD:
                    node.deleted = True
                    return True
                if not node.deleted:
                    return True
                else:
                    return False
            else:
                return False

    def postOrder(self, node=None):
        if node is None:
            node = self.root
        if node.right is not None or node.left is not None:
            left_str = None
            right_str = None

            if node.left is not None:
                left_str = self.postOrder(node.left)

            if node.right is not None:
                right_str = self.postOrder(node.right)

            if left_str is None:
                return f"{right_str} {node.value}"
            elif right_str is None:
                return f"{left_str} {node.value}"
            else:
                if node.deleted:
                    node.value = str(node.value) + "D"
                return f"{left_str} {right_str} {node.value}"  
        else:
            if node.deleted:
                node.value = str(node.value) + "D"
            return node.value

        
    def preOrder(self, node=None):
        if node is None:
            node = self.root
        if node.right is not None or node.left is not None:
            left_str = None
            right_str = None

            if node.left is not None:
                left_str = self.preOrder(node.left)

            if node.right is not None:
                right_str = self.preOrder(node.right)

            if left_str is None:
                return f"{node.value} {right_str}"
            elif right_str is None:
                return f"{node.value} {left_str}"
            else:
                return f"{node.value} {left_str} {right_str}"  
        else:
            return node.value
    def inOrder(self, node=None):
        if node is None:
            node = self.root
        if node.right is not None or node.left is not None:
            left_str = None
            right_str = None

            if node.left is not None:
                left_str = self.inOrder(node.left)

            if node.right is not None:
                right_str = self.inOrder(node.right)

            if left_str is None:
                if node.deleted:
                    tmp = str(node.value) + "D"
                    return f"{tmp} {right_str}"
                else:
                    return f"{node.value} {right_str}"
            elif right_str is None:
                if node.deleted:
                    tmp = str(node.value) + "D"
                    return f"{left_str} {tmp}"
                else:
                    return f"{left_str} {node.value}"
            else:
                if node.deleted:
                    tmp = str(node.value) + "D"
                    return f"{left_str} {tmp} {right_str}"
                else:
                    return f"{left_str} {node.value} {right_str}"
        else:
            if node.deleted:
                tmp = str(node.value) + "D"
                return tmp
            else:
                return node.value

    def findLarger(self, value, node=None, max=-1):
        if node is None:
            node = self.root
        if node.right is not None or node.left is not None:
            if node.left is not None:
                max = self.findLarger(value, node.left, max)

            if node.right is not None:
                max = self.findLarger(value, node.right, max)

            if node.value >= value:
                if max == -1:
                    max = node.value
                elif node.value < max:
                    max = node.value
            return max
        else:
            if node.value >= value:
                if max == -1:
                    max = node.value
                elif node.value < max:
                    max = node.value
            return max

    def removeLarger(self, value):
        tmp = self.findLarger(value)
        self.removeValue(tmp)
        return tmp