from segmentIntersection import segmentIntersection, getIntersectionPoints
from utils import segmentFactory, drawResults, saveSegments, getSegments
from model.Event import Event
from AVLTree.AVLTree import AVLTree
from utils import appendIfNotInList

segments = getSegments()
Q = AVLTree()
for i in range(0,len(segments)):
    Q.insert(Event(segments[i].pt1))
    Q.insert(Event(segments[i].pt2))

intersectionPoints = segmentIntersection(segments)

saveSegments(segments)

bruteForce = []
for segment1 in segments:
    for segment2 in segments:
        if segment1 == segment2:
            break
        for temp in getIntersectionPoints(segment1,segment2):
            appendIfNotInList(bruteForce, temp)

bruteForce.sort()
intersectionPoints.sort()

if bruteForce != intersectionPoints:
    print("You did not find all intersection points")
    print(f'Brute Force: Found {len(bruteForce)} intersections!')
    print(f'Sweepline: Found {len(intersectionPoints)} intersections!')

drawResults(segments, intersectionPoints, "Sweep Line")
drawResults(segments, bruteForce, "Brute Force")