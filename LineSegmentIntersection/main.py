from utils import segmentFactory
from bintrees import AVLTree

segments = segmentFactory(0,100,0,100,5, 0)
Q = AVLTree()
for i in range(0,len(segments)):
    segments[i].print()
    Q.insert(segments[i].pt1,i)
    Q.insert(segments[i].pt2,2*i-1)

print(Q.max_item())