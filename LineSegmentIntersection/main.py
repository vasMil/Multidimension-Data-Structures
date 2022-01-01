from utils import segmentFactory
from model.Event import Event
from avlTree.AVLTree import AVLTree

# Debug insert, rebalance, predecessor, successor, inorder traversal
segments = segmentFactory(0,100,0,100,50, 0)
Q = AVLTree()
for i in range(0,len(segments)):
    Q.insert(Event(segments[i].pt1))
    Q.insert(Event(segments[i].pt2))

# i = 0
# for data in Q.inOrder():
#     print(str(i) + '. ' + data.point.toString())
#     i+=1

# print("Successor of " + segments[2].pt2.toString() + " is:")
# succ = Q.getSuccessor(Event(segments[2].pt2))
# if succ:
#     succ.data.point.print()
# else:
#     print("None")

# print("Predecessor of " + segments[0].pt1.toString() + " is:")
# pred = Q.getPredecessor(Event(segments[0].pt1))
# if pred:
#     pred.data.point.print()
# else:
#     print("None")

# Debug delete
# Q = AVLTree()
# testNodeData = [31, 18, 47, 7, 25, 34, 62, 28, 59, 88, 33, 95]
# for data in testNodeData:
#     Q.insert(data)
# print("Test tree before:")
# Q.inOrderPrint()

# Debug deletion of a leaf
# dataToDelete = [28, 25, 7]
# for data in dataToDelete:
#     Q.delete(data)
#     print("Test tree after deleting " + str(data))
#     Q.inOrderPrint()

# Debug deletion of a node with a single child
# dataToDelete = [25, 34, 47]
# for data in dataToDelete:
#     Q.delete(data)
#     print("Test tree after deleting " + str(data))
#     Q.inOrderPrint()

# Debug deletion of a node with two children
# dataToDelete = [47, 31]
# for data in dataToDelete:
#     Q.delete(data)
#     print("Test tree after deleting " + str(data))
#     Q.inOrderPrint()
