from utils import segmentFactory
from Event import Event
from avlTree.AVLTree import AVLTree

segments = segmentFactory(0,100,0,100,50, 0)
Q = AVLTree()
for i in range(0,len(segments)):
    segments[i].print()
    Q.insert(Event(segments[i].pt1))
    Q.insert(Event(segments[i].pt2))

Q.inOrderPrint()
print("Successor of " + segments[2].pt2.toString() + " is:")
succ = Q.getSuccessor(Event(segments[2].pt2))
if succ:
    succ.data.point.print()
else:
    print("None")

print("Predecessor of " + segments[0].pt1.toString() + " is:")
pred = Q.getPredeccessor(Event(segments[0].pt1))
if pred:
    pred.data.point.print()
else:
    print("None")
# i = 0
# for data in Q.inOrder():
#     print(str(i) + '. ' + data.point.toString())
#     i+=1

