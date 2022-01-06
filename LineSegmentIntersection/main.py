import utils
from segmentIntersection import segmentIntersection, getIntersectionPoints

while True:
    segments = utils.getSegments()
    intersectionPoints = segmentIntersection(segments)

    bruteForce = []
    for segment1 in segments:
        for segment2 in segments:
            if segment1 == segment2:
                break
            for temp in getIntersectionPoints(segment1,segment2):
                utils.appendIfNotInList(bruteForce, temp)

    bruteForce.sort()
    intersectionPoints.sort()
    if bruteForce != intersectionPoints:
        break


if bruteForce != intersectionPoints:
    print("You did not find all intersection points")
    utils.saveSegments(segments)

    print("\n SEGMENTS \n")
    for segment in segments:
        segment.print()

    print("\n INTERSECTION POINTS \n")
    for point in bruteForce:
        point.print()

    utils.drawResults(segments, bruteForce, "Brute Force")

print(f'Brute Force: Found {len(bruteForce)} intersections!')
print(f'Sweepline: Found {len(intersectionPoints)} intersections!')

utils.drawResults(segments, intersectionPoints, "Sweep Line")

for segment1 in segments:
    for segment2 in segments:
        count = 0
        if segment1 == segment2:
            count += 1
        if count == 2:
            raise "There are two identical segments"
