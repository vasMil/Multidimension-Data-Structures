class Node:
    def __init__(self, data = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

    def getHeight(self):
        if not self.leftChild and not self.rightChild:
            self.height = 1
        elif not self.leftChild:
            self.height = 1 + self.rightChild.getHeight()
        elif not self.rightChild:
            self.height = 1 + self. leftChild.getHeight()
        else:
            self.height = 1 + max(self.leftChild.getHeight(),
                                  self.rightChild.getHeight())

        return self.height


    def getBalance(self):
        if not self.leftChild and not self.rightChild:
            return 0
        elif not self.leftChild:
            return - self.rightChild.getHeight()
        elif not self.rightChild:
            return self.leftChild.getHeight()
        else:
            return self.leftChild.getHeight() - self.rightChild.getHeight()