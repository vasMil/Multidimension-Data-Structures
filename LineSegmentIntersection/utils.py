import random
from Point import Point
from Segment import Segment

def segmentFactory(minx,maxx,miny,maxy, numOfSegments):
    segments = [Segment(Point(0,0),Point(0,0))] * numOfSegments
    for i in range(0, numOfSegments):
        pt = [Point(0,0)]*2
        for j in range(0,2):
            pt[j] = Point(round(random.uniform(minx,maxx),2), round(random.uniform(miny,maxy),2))
        segments[i] = Segment(pt[0], pt[1])
    return segments
