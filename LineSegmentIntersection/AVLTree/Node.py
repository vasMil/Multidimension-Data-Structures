class Node:
    def __init__(self, data = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

    def updateHeight(self):
        if not self.leftChild and not self.rightChild:
            self.height = 1
        elif not self.leftChild:
            self.height = 1 + self.rightChild.height
        elif not self.rightChild:
            self.height = 1 + self.leftChild.height
        else:
            self.height = 1 + max(self.leftChild.height,
                                  self.rightChild.height)

        return self.height


    def getBalance(self):
        if not self.leftChild and not self.rightChild:
            return 0
        elif not self.leftChild:
            return - self.rightChild.height
        elif not self.rightChild:
            return self.leftChild.height
        else:
            return self.leftChild.height - self.rightChild.height


    def numOfChildren(self):
        if self.rightChild and self.leftChild:
            return 2
        if not self.rightChild and not self.leftChild:
            return 0
        return 1