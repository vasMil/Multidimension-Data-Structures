from .Node import Node

class AVLTree:
    def __init__(self, root = None):
        self.root = root


    def insert(self, data):
        path = self.searchPath(data)
        if not path:
            self.root = Node(data)
            return
        parent = path.pop()
        if(data < parent.data):
            parent.leftChild = Node(data)
        else:
            parent.rightChild = Node(data)

        parent.updateHeight()

        # Balance
        for i in reversed(range(0,len(path))):
            curNode = path[i]
            if curNode.getBalance() > 1 or curNode.getBalance() < -1:
                if i - 1 < 0:
                    self.root = self.getTreeBalanced(curNode)
                elif (path[i].data < path[i-1].data):
                    path[i-1].leftChild = self.getTreeBalanced(curNode)
                else:
                    path[i-1].rightChild = self.getTreeBalanced(curNode)
            else:
                curNode.updateHeight()


    def getTreeBalanced(self, node):
        balance = node.getBalance()
        if balance > 1:
            if node.leftChild.getBalance() < 0:
                node.leftChild = self.leftRotate(node.leftChild)
            return self.rightRotate(node)
        elif balance < -1:
            if node.rightChild.getBalance() > 0:
                node.rightChild = self.rightRotate(node.rightChild)
            return self.leftRotate(node)


    def leftRotate(self, node):
        # Get nodes you are going to rotate
        x = node.rightChild
        y = x.leftChild
        # Rotate
        x.leftChild = node
        node.rightChild = y
        # Update heights
        if y: y.updateHeight()
        node.updateHeight()
        return x


    def rightRotate(self, node):
        # Get nodes you are going to rotate
        x = node.leftChild
        y = x.rightChild
        # Rotate
        x.rightChild = node
        node.leftChild = y
        # Update heights
        node.updateHeight()
        if x: x.updateHeight()
        return x


    def searchPath(self, data):
        if not self.root:
            return []
        path = []
        curNode = self.root
        while(curNode):
            path.append(curNode)
            if(data < curNode.data):
                curNode = curNode.leftChild
            else:
                curNode = curNode.rightChild
        return path


    def inOrder(self):
        inOrderList = []
        path = []
        curNode = self.root

        while True:
            if curNode:
                path.append(curNode)
                curNode = curNode.leftChild
            elif path:
                curNode = path.pop()
                inOrderList.append(curNode.data)
                curNode = curNode.rightChild
            else:
                break

        return inOrderList


    def inOrderPrint(self):
        path = []
        curNode = self.root

        while True:
            if curNode:
                path.append(curNode)
                curNode = curNode.leftChild
            elif path:
                curNode = path.pop()
                print("Value: " + curNode.data.point.toString() + ", Height: " + str(curNode.height))
                curNode = curNode.rightChild
            else:
                break