from AVLTree.AVLTree import AVLTree
from model.Event import Event
from model.Point import Point
from utils import appendIfNotInList

def segmentIntersection(segments):
    statusTree = AVLTree()
    eventTree = AVLTree()
    intersPoints = []

    for segment in segments:
        registerEventInTree(eventTree, Event(segment.pt1), [segment])
        registerEventInTree(eventTree, Event(segment.pt2), [segment])

    while eventTree.root:
        event = eventTree.popLargest()
        handleEvent(event, eventTree, statusTree, intersPoints)
    return intersPoints


def handleEvent(event, eventTree, statusTree, logger):
    if len(event.lowerPointArr) + len(event.upperPointArr) + len(event.liesInsideArr) > 1:
        logger.append(event.point)
    statusTree.deleteArray(event.lowerPointArr)
    updateCompDataInStatusTree(statusTree, event.liesInsideArr, event)
    soft_updateCompData(statusTree.inOrder(), event)
    statusTree.insertArray(event.upperPointArr)
    if len(event.upperPointArr) + len(event.liesInsideArr) == 0:
        curSegment = event.lowerPointArr[0]
        pred = statusTree.getNextSmallestData(curSegment)
        succ = statusTree.getNextLargestData(curSegment)
        if pred and succ: findNewIntersection(pred, succ, event, eventTree, logger)
    else:
        upperUinside = event.upperPointArr + event.liesInsideArr
        upperUinside.sort()
        s = upperUinside[0]
        sl = statusTree.getNextSmallestData(s)
        if sl: findNewIntersection(s,sl,event,eventTree, logger)
        s = upperUinside[-1]
        sr = statusTree.getNextLargestData(s)
        if sr: findNewIntersection(s, sr, event, eventTree, logger)


def updateCompDataInStatusTree(statusTree, segments, event):
    for segment in segments:
        statusTree.delete(segment)
    for segment in segments:
        segment.updateComparissonData(event.point.y, event.point.x)
    for segment in segments:
        statusTree.insert(segment)
    return

def soft_updateCompData(segments, event):
    for segment in segments:
        segment.updateComparissonData(event.point.y, event.point.x)

def findNewIntersection(segment1, segment2, event, eventTree, logger):
    points = getIntersectionPoints(segment1, segment2)
    for point in points:
        if isNewIntersection(point, event):
            registerEventInTree(eventTree, Event(point), [segment1, segment2])
        # TODO: Check if the statement below is correct, since it is your addition
        # Required so I can detect and report the intersection point between
        # pt15 = Point(2,1); pt16 = Point(2,0); s8 = Segment(pt15,pt16)
        # pt17 = Point(2,0.4); pt18 = Point(1,0.3); s9 = Segment(pt17,pt18)
        elif event.point == point and segment1.includes(point) and segment2.includes(point):
            appendIfNotInList(logger, event.point)


# If it is above the sweep line on it and on the right of the event then it is new
def isNewIntersection(intersectionPoint, event):
    if intersectionPoint.y < event.point.y or (intersectionPoint.y == event.point.y and intersectionPoint.x > event.point.x):
        return True
    return False


# Insert event in tree.
# If the event already exists append the segment in the correct list
def registerEventInTree(tree, event, segments):
    registeredEvent = tree.search(event)
    if registeredEvent:
        for segment in segments:
            updateEventArrays(registeredEvent, segment)
        return
    for segment in segments:
        updateEventArrays(event, segment)
    tree.insert(event)


def updateEventArrays(event, segment):
    if event.point == segment.pt1:
        appendIfNotInList(event.upperPointArr, segment)
    elif event.point == segment.pt2:
        appendIfNotInList(event.lowerPointArr, segment)
    else:
        appendIfNotInList(event.liesInsideArr, segment)


# Counter-clockwise: -1
# Collinear: 0
# Clockwise: 1
def orientation(segment, point):
    a = segment.pt1; b = segment.pt2; c = point
    crossProd = (b.x - c.x)*(a.y - c.y) - (a.x - c.x)*(b.y-c.y)
    if crossProd < 0:
        return -1
    elif crossProd == 0:
        return 0
    return 1


# Implements the tactics required to determine whether there is an intersection point or not
# If there is one it uses getInstersectionPoint to find it and returns it inside a list
# If there in not one returns an empty list
# In the case that two segments overlap return both those endpoints that are inside another segment
def getIntersectionPoints(segment1, segment2):
    orient12_1 = orientation(segment1, segment2.pt1)
    orient12_2 = orientation(segment1, segment2.pt2)
    if orient12_1 == orient12_2:
        # Both 0 -> Check if segments overlap
        if not(orient12_1 or orient12_2):
            return getIntersectionPointsForCollinearSegments(segment1, segment2)
        # Both counter-clockwise or clockwise -> Cannot intersect
        return []
    # C - CC || CC - C || CO - C || C - CO || CO - CC || CC - CO

    orient1_12 = orientation(segment2, segment1.pt1)
    orient2_12 = orientation(segment2, segment1.pt2)
    if orient1_12 == orient2_12:
        # Both 0 -> Check if segments overlap
        if not(orient1_12 or orient2_12):
            return getIntersectionPointsForCollinearSegments(segment1, segment2)
        # Both counter-clockwise or clockwise -> Cannot intersect
        return []
    # C - CC || CC - C || CO - C || C - CO || CO - CC || CC - CO

    # Combinations that reach this point are either impossible to happen
    # (ex. (Clockwise - 0 and 0 - CounterClockwise), thus I need not to worry about them)
    # or there is an intersection between the two segments
    return [getIntersectionPoint(segment1, segment2)]


# Returns the intersection point of the two given segments
# I will be assuming there is one and thus I may consider the two segments
# as lines.
# Since two lines that intersect may only do so at a single point, the segments
# from which I derived the lines should also intersect at a single point.
# If the above assumption is wrong, that is the two segments do not intersect,
# function will either return a point that does not lie inside any of the two segments or
# None, in the case they are parallel.
def getIntersectionPoint(segment1, segment2):
    xdif1 = segment1.pt2.x - segment1.pt1.x
    ydif1 = segment1.pt2.y - segment1.pt1.y
    xdif2 = segment2.pt2.x - segment2.pt1.x
    ydif2 = segment2.pt2.y - segment2.pt1.y

    det = ydif1*xdif2 - ydif2*xdif1

    if not det:
        # segments are parallel
        return None

    # The two segments are not parallel and thus det != 0
    x = ((segment2.pt1.y - segment1.pt1.y)*xdif1*xdif2 + segment1.pt1.x*ydif1*xdif2 - segment2.pt1.x*xdif1*ydif2) / det
    if not xdif1:
        y = ydif2/xdif2 * x + segment2.pt1.y - ydif2/xdif2 * segment2.pt1.x
    else:
        # May not both be horizontal (since they are not collinear)
        y = ydif1 / xdif1 * x + segment1.pt1.y - ydif1 / xdif1 * segment1.pt1.x
    return Point(x,y)


# Consider the different cases of the two segments overlapping
# (return the endpoints of the segments that are in the overlap)
def getIntersectionPointsForCollinearSegments(segment1, segment2):
    # If segments have a common endpoint return it in a list
    if segment1.pt2 == segment2.pt1:
        return [segment1.pt2]
    elif segment2.pt2 == segment1.pt1:
        return [segment1.pt1]

    # Segments do not have a common endpoint, thus two points should be returned
    intersectionPoints = []
    if collinearPointLiesInsideSegment(segment1, segment2.pt1):
        intersectionPoints.append(segment2.pt1)
    if collinearPointLiesInsideSegment(segment1, segment2.pt2):
        intersectionPoints.append(segment2.pt2)
    if collinearPointLiesInsideSegment(segment2, segment1.pt1):
            intersectionPoints.append(segment1.pt1)
    if collinearPointLiesInsideSegment(segment2, segment1.pt2):
        intersectionPoints.append(segment1.pt2)
    return intersectionPoints


# Returns True if the point lies inside segment
# Since I know all three points lie in the same line
# I only need to check whether the projections of the point
# on the x axis and on the y axis lie inside the projection of the segment of each axis
                        # General Case
                        # |
                        # -- - - - - - - B   <- segment.pt1
                        # |             /|
                        # -- - - - - - C |   <- point
                        # |           /| |
                        # -- - - - - A | |   <- segment.pt2
                        # |         /| | |
                        # + ---------|-|-|---------
def collinearPointLiesInsideSegment(segment, point):
    xaxis_ok = False
    yaxis_ok = False
    if segment.pt1.x > segment.pt2.x:
        if segment.pt1.x >= point.x and segment.pt2.x <= point.x:
            xaxis_ok = True
    else:
        if segment.pt2.x >= point.x and segment.pt1.x <= point.x:
            xaxis_ok = True

    if segment.pt1.y > segment.pt2.y:
        if segment.pt1.y >= point.y and segment.pt2.y <= point.y:
            yaxis_ok = True
    else:
        if segment.pt2.y >= point.y and segment.pt1.y <= point.y:
            yaxis_ok = True

    if xaxis_ok and yaxis_ok:
        return True
    return False
