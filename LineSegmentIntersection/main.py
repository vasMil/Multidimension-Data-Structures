from utils import segmentFactory
from Event import Event
from avlTree.AVLTree import AVLTree



segments = segmentFactory(0,100,0,100,50, 0)
Q = AVLTree()
for i in range(0,len(segments)):
    Q.insert(Event(segments[i].pt1))
    Q.insert(Event(segments[i].pt2))

Q.inOrder(Q.root)

