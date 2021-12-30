from .Node import Node

class AVLTree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, data):
        if (self.root == None):
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curNode):
        if not curNode:
            return Node(data)
        elif (data < curNode.data):
            curNode.leftChild = self._insert(data, curNode.leftChild)
        else:
            curNode.rightChild = self._insert(data, curNode.rightChild)

        curNode.height = curNode.getHeight()

        balance = curNode.getBalance()

        if balance > 1 and data < curNode.leftChild.data:
            return self.rightRotate(curNode)
        if balance < -1 and data > curNode.rightChild.data:
            return self.leftRotate(curNode)
        if balance > 1 and curNode.rightChild and data > curNode.leftChild.data:
            curNode.leftChild = self.leftRotate(curNode.leftChild)
            return self.rightRotate(curNode)
        if balance < -1 and curNode.leftChild and data < curNode.leftChild.data:
            curNode.rightChild = self.rightRotate(curNode.rightChild)
            return self.leftRotate(curNode)

        return curNode

    def leftRotate(self, node):
        y = node.rightChild
        x = y.leftChild

        y.leftChild = node
        node.rightChild = x

        node.getHeight()
        y.getHeight()

        return y

    def rightRotate(self, node):
        x = node.leftChild
        y = x.rightChild

        x.right = node
        node.leftChild = y

        node.getHeight()
        x.getHeight()

        return x

    def inOrder(self, root):
        if not root:
            return

        self.inOrder(root.leftChild)
        print("{0} ".format(root.data), end="")
        self.inOrder(root.rightChild)