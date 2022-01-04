from .Node import Node

class AVLTree:
    def __init__(self, root = None):
        if root:
            self.root = Node(root)
        else:
            self.root = None


    def insert(self, data):
        # Find the path to the node with node.data closest to data
        path = self.searchPath(data)
        if not path:
            # There is no root to start my search from - assign data to a Node and that noda as the root of my tree
            self.root = Node(data)
            return
        # Decide whether the new node should be the rightChild or the leftChild of it's parent
        parent = path.pop()
        if data < parent.data:
            parent.leftChild = Node(data)
        else:
            parent.rightChild = Node(data)
        # Update the height of it's parent
        parent.updateHeight()

        # Balance path - starting from bottom to root
        for i in reversed(range(0,len(path))):
            curNode = path[i]
            if curNode.getBalance() > 1 or curNode.getBalance() < -1:
                # Should only get here once
                if i - 1 < 0:
                    # Only one element left in path (and that is the root). Balance it
                    self.root = self.getTreeBalanced(curNode)
                elif path[i].data < path[i-1].data:
                    # curNode is the leftChild of it's parent
                    path[i-1].leftChild = self.getTreeBalanced(curNode)
                else:
                    # curNode is the rightChild of it's parent
                    path[i-1].rightChild = self.getTreeBalanced(curNode)
            else:
                # It is balanced, update curNode.height, since the height of one of it's children changed,
                # it's height might have also changed
                curNode.updateHeight()


    def delete(self, data):
        # find node containing data
        path = self.searchPath(data)
        if not path: return

        node = path.pop()
        # Attempting to require as little operator overloads as possible
        if not(node.data == data):
            # Could not find data
            return

        # Handle special case of root (has no parent to pop())
        if node == self.root:
            if node.numOfChildren() == 0:
                    self.root = None
            elif node.numOfChildren() == 1:
                if node.leftChild:
                    self.root = node.leftChild
                else:
                    self.root = node.rightChild
            else:
                successor = self.getSuccessor(node.data)
                self.delete(successor.data)
                successor.leftChild = node.leftChild
                successor.rightChild = node.rightChild
                node.updateHeight()
                node.data = successor.data
            return


        parent = path.pop()
        if node.numOfChildren() == 0:
            # Just remove the node
            if node.data < parent.data:
                parent.leftChild = None
            else:
                parent.rightChild = None

        elif node.numOfChildren() == 1:
            # Replace the node being removed with it's child
            if node.data < parent.data:
                # node is the leftChild of it's parent
                if node.rightChild:
                    # node has a rightChild
                    parent.leftChild = node.rightChild
                else:
                    # node has a leftChild
                    parent.leftChild = node.leftChild
            else:
                # node is the rightChild of it's parent
                if node.rightChild:
                    # node has a rightChild
                    parent.rightChild = node.rightChild
                else:
                    # node has a leftChild
                    parent.rightChild = node.leftChild

        else:
            # Successor is the leftmost leaf of node's right child
            successor = self.getSuccessor(node.data)
            self.delete(successor.data)
            # Reattach node's left and right branches
            successor.leftChild = node.leftChild
            successor.rightChild = node.rightChild
            if node.data < parent.data:
                parent.leftChild = successor
            else:
                parent.rightChild = successor
            successor.updateHeight()


        # Rebalance path to root - same for all cases
        curNode = parent
        while path:
            curNode.updateHeight()
            curNode = parent
            parent = path.pop()
            if curNode.data < parent.data:
                parent.leftChild = self.getTreeBalanced(curNode)
            else:
                parent.rightChild = self.getTreeBalanced(curNode)
        self.root = self.getTreeBalanced(self.root)
        self.root.updateHeight()


    def insertArray(self, dataArray):
        for data in dataArray:
            self.insert(data)


    def deleteArray(self, dataArray):
        for data in dataArray:
            self.delete(data)


    # Decides for the rotation tactic
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
        return node


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

    # Returns the path from root to the node that contains data
    # or if data not in node, the last explored leaf
    def searchPath(self, data):
        if not self.root:
            return None
        path = []
        curNode = self.root
        while curNode:
            path.append(curNode)
            if data < curNode.data:
                curNode = curNode.leftChild
            elif data > curNode.data:
                curNode = curNode.rightChild
            else:
                break
        return path

    # Returns the inorder successor of the node that contains data
    def getSuccessor(self, data, path = None):
        if not self.root:
            return None
        if not path:
            path = self.searchPath(data)
        i = len(path) - 1
        if path[i].rightChild:
            # path[i] is the node that either contains data or is the leaf closest to data
            # thus if there is a right child you should return it's leftmost leaf as the successor
            succ = path[i].rightChild
            while succ.leftChild:
                succ = succ.leftChild
            return succ
        if len(path) > 1:
            # path[i] has no rightChild - the successor (if one) is the first parent,
            # found in the path from the node, that contains data, to the root, whose leftChild
            # is in searchPath
            while i > 0:
                if path[i-1].data > path[i].data:
                    return path[i-1]
                i -= 1
        # If there is no node with data greater than data
        return None

    # Returns the inorder predecessor of the node that contains data
    def getPredecessor(self, data, path = None):
        if not self.root:
            return None
        if not path:
            path = self.searchPath(data)
        i = len(path) - 1
        if path[i].leftChild:
            # Get the rightmost leaf of the subtree with root node's leftChild
            pred = path[i].leftChild
            while pred.rightChild:
                pred = pred.rightChild
            return pred
        if len(path) > 1:
            # Get the first parent that has path as part of it's rightChild
            while i > 0:
                if not (path[i-1].data > path[i].data): # aka path[i-1] <= path[i] -> Parent (i-1) has child (i) on the right
                    return path[i-1]
                i -= 1
        return None


    def getPredecessorData(self, data, path = None):
        node = self.getPredecessor(data, path)
        if node: return node.data
        return None

    def getSuccessorData(self,data, path = None):
        node = self.getSuccessor(data, path)
        if node: return node.data
        return None


    def getNextLargestData(self, data):
        if not self.root:
            return None
        path = self.searchPath(data)
        finalNode = path[len(path) - 1]
        if finalNode.data == data:
            return self.getSuccessorData(data, path)
        # Data not in tree
        if data < finalNode.data:
            # Data would be on the leftChild of the final node and thus (since it would be a leaf)
            # the next largest value is it's parent
            return finalNode.data
        # Data would be on the rightChild of the final node and thus it's successor should be the successor of the
        # final node (since data is NOT in the tree)
        return self.getSuccessorData(finalNode.data, path)


    def getNextSmallestData(self, data):
        if not self.root:
            return None
        path = self.searchPath(data)
        finalNode = path[len(path) - 1]
        if finalNode.data == data:
            return self.getPredecessorData(data, path)
        # Data not in tree
        if data < finalNode.data:
            # Data would be on the leftChild of the final node and thus (since it would be a leaf)
            # thus it's predecessor would be the current predecessor of finalNode
            return self.getPredecessorData(finalNode.data, path)
        # Data would be on the rightChild of the final node and thus it's predecessor should be it's the parent
        # (since it would be a leaf)
        return finalNode.data


    # Deletes node and returns smallest node.data in tree
    def popSmallest(self):
        curNode = self.root
        curMin = self.root
        while curNode:
            curMin = curNode
            curNode = curNode.leftChild
        self.delete(curMin.data)
        return curMin.data

    # Deletes node and returns largest node.data in tree
    def popLargest(self):
        curNode = self.root
        curMax = self.root
        while curNode:
            curMax = curNode
            curNode = curNode.rightChild
        self.delete(curMax.data)
        return curMax.data

    # Searches for a specific value in the tree, if it finds it, returns the data
    # else returns None
    def search(self, data):
        curNode = self.root
        while curNode:
            if curNode.data == data:
                return curNode.data
            if data < curNode.data:
                curNode = curNode.leftChild
            else:
                curNode = curNode.rightChild
        return None


    # Returs the inorder traversal of the tree as a list (it is obviously sorted)
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

    # Prints the inorder traversal (does not return the list)
    def inOrderPrint(self):
        path = []
        curNode = self.root

        while True:
            if curNode:
                path.append(curNode)
                curNode = curNode.leftChild
            elif path:
                curNode = path.pop()
                print("Value: " + str(curNode.data) + ", Height: " + str(curNode.height))
                curNode = curNode.rightChild
            else:
                break