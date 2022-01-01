import random
from model.Point import Point
from model.Segment import Segment

def segmentFactory(minx,maxx,miny,maxy, numOfSegments, round_n_digits = 2):
    segments = [Segment(Point(0,0),Point(0,0))] * numOfSegments
    for i in range(0, numOfSegments):
        pt = [Point(0,0)]*2
        for j in range(0,2):
            if (round_n_digits == 0):
                pt[j] = Point(random.randint(minx, maxx), random.randint(miny, maxy))
            else:
                pt[j] = Point(round(random.uniform(minx,maxx),round_n_digits),
                              round(random.uniform(miny,maxy),round_n_digits))
        segments[i] = Segment(pt[0], pt[1])
    return segments