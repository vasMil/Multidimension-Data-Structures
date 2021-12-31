from utils import segmentFactory
from Event import Event
from avlTree.AVLTree import AVLTree

segments = segmentFactory(0,100,0,100,5, 0)
Q = AVLTree()
for i in range(0,len(segments)):
    segments[i].print()
    Q.insert(Event(segments[i].pt1))
    Q.insert(Event(segments[i].pt2))

Q.inOrderPrint()
Q.inOrder()
# i = 0
# for data in Q.inOrder():
#     print(str(i) + '. ' + data.point.toString())
#     i+=1

