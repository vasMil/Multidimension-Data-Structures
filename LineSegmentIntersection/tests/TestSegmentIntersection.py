import unittest
from model.Point import Point
from model.Segment import Segment
import segmentIntersection

class TestIntersection(unittest.TestCase):

    def test_segmentIntersection(self):
        # Test 1, graph view here: https://www.desmos.com/calculator/okwckrxwug
        pt1 = Point(-1,1); pt2 = Point(5,2); s1 = Segment(pt1,pt2)
        pt3 = Point(2,2); pt4 = Point(1,1); s2 = Segment(pt3,pt4)
        pt5 = Point(1.2,1.6); pt6 = Point(1.4,1.4); s3 = Segment(pt5,pt6)
        pt7 = Point(1.4,1.2); pt8 = Point(1.1,1.5); s4 = Segment(pt7,pt8)
        pt9 = Point(1.4,1.5); pt10 = Point(1.4,2); s5 = Segment(pt9,pt10)
        pt11 = Point(1.3,1.305); pt12 = Point(1.3,1.38); s6 = Segment(pt11,pt12)
        pt13 = Point(1.295,1.34); pt14 = Point(1.305,1.34); s7 = Segment(pt13,pt14)
        pt15 = Point(2,1); pt16 = Point(2,0); s8 = Segment(pt15,pt16)
        pt17 = Point(2,0.4); pt18 = Point(1,0.3); s9 = Segment(pt17,pt18)
        pt19 = Point(2,0.2); pt20 = Point(1.8,0.1); s10 = Segment(pt19,pt20)
        pt21 = Point(2,0.2); pt22 = Point(2.4,0.1); s11 = Segment(pt21,pt22)

        expectedPoints = [Point(1.4,1.4), Point(1.3,1.3), Point(1.3, 1.34), Point(2,0.4), Point(2,0.2), Point(1.229, 1.371)]
        expectedPoints.sort()

        results = segmentIntersection.segmentIntersection([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11])
        results.sort()

        for i in range(0,len(expectedPoints)):
            if expectedPoints[i] == Point(1.229, 1.371):
                self.assertAlmostEqual(first = expectedPoints[i].x, second = results[i].x, delta = 0.01)
                self.assertAlmostEqual(first = expectedPoints[i].y, second = results[i].y, delta = 0.01)
            else:
                self.assertEqual(expectedPoints[i], results[i])

        # Test2 -> https://www.desmos.com/calculator/etlaxwhbk2
        pt1 = Point(45,-50); pt2 = Point(60,-52); s1 = Segment(pt1,pt2)
        pt3 = Point(55,-50); pt4 = Point(55,-55); s2 = Segment(pt3,pt4)
        pt5 = Point(45,-52); pt6 = Point(52,-52); s3 = Segment(pt5,pt6)
        pt7 = Point(50,-52); pt8 = Point(65,-52); s4 = Segment(pt7,pt8)
        pt9 = Point(53.8,-53.9); pt10 = Point(56.5,-55.25); s5 = Segment(pt9,pt10)
        pt11 = Point(55,-54); pt12 = Point(55,-55); s6 = Segment(pt11,pt12)
        pt13 = Point(54,-55); pt14 = Point(56,-54); s7 = Segment(pt13,pt14)
        pt15 = Point(54,-54.5); pt16 = Point(56.5,-54.5); s8 = Segment(pt15,pt16)

        expectedPoints = [Point(55,-51.3333333), Point(50,-52), Point(52,-52), Point(55,-52), Point(60,-52),
                          Point(55,-54.5)]
        expectedPoints.sort()

        results = segmentIntersection.segmentIntersection([s1,s2,s3,s4,s5,s7])
        results.sort()

        for i in range(0,len(expectedPoints)):
            if expectedPoints[i] == Point(55,-51.3333333):
                self.assertAlmostEqual(first = expectedPoints[i].x, second = results[i].x, delta = 0.01)
                self.assertAlmostEqual(first = expectedPoints[i].y, second = results[i].y, delta = 0.01)
            else:
                self.assertEqual(expectedPoints[i], results[i])

        # Test3 -> Overlaps -> https://www.desmos.com/calculator/uzibw0g05n
        pt1 = Point(-10,-2); pt2 = Point(-8,-2); s1 = Segment(pt1,pt2)
        pt3 = Point(-9,-2); pt4 = Point(-2,-2); s2 = Segment(pt3,pt4)
        pt5 = Point(-6,-2); pt6 = Point(-4,-2); s3 = Segment(pt5,pt6)
        pt7 = Point(-5,0); pt8 = Point(-5,-4); s4 = Segment(pt7,pt8)
        pt9 = Point(-5,-1); pt10 = Point(-5,-3); s5 = Segment(pt9,pt10)
        pt11 = Point(-5,-3.5); pt12 = Point(-5,-6); s6 = Segment(pt11,pt12)
        pt13 = Point(0,0); pt14 = Point(6,6); s7 = Segment(pt13,pt14)
        pt15 = Point(4,4); pt16 = Point(5,5); s8 = Segment(pt15,pt16)
        pt17 = Point(2,2); pt18 = Point(-1,-1); s9 = Segment(pt17,pt18)

        expectedPoints = [Point(-9,-2), Point(-8,-2), Point(-6,-2), Point(-5,-1), Point(-4,-2), Point(-5,-3),
                          Point(-5,-3.5), Point(-5,-4), Point(-5,-2), Point(4,4), Point(5,5), Point(2,2), Point(0,0)]
        expectedPoints.sort()

        results = segmentIntersection.segmentIntersection([s1,s2,s3,s4,s5,s6,s7,s8,s9])
        results.sort()

        for i in range(0,len(expectedPoints)):
            self.assertEqual(expectedPoints[i], results[i])

    def test_getIntersectionPoint(self):
        # vertical segment
        pt1 = Point(0,0); pt2 = Point(0, 10); s1 = Segment(pt1, pt2)
        # horizontal segment
        pt3 = Point(1,1); pt4 = Point(-1,1); s2 = Segment(pt3, pt4)
        # positive slope
        pt5 = Point(1,10); pt6 = Point(-1,0); s3 = Segment(pt5, pt6)
        # negative slope
        pt7 = Point(0,6); pt8 = Point(1,1); s4 = Segment(pt7, pt8)
        # end point overlapping
        pt9 = Point(0,0); pt10 = Point(-1,-1); s5 = Segment(pt9, pt10)
        # not intersecting pt1

        # Configure parallel arrays for the loop
        arg1 = [s1, s1, s1, s1, s2, s2]
        arg2 = [s2, s3, s4, s5, s3, s4]
        expectAns = [Point(0,1), Point(0,5), Point(0,6), Point(0,0), Point(-0.8, 1), Point(1,1)]

        for i in range(0,len(arg1)):
            self.assertEqual(expectAns[i], segmentIntersection.getIntersectionPoint(arg1[i], arg2[i]))


    def test_getIntersectionPointsForCollinearSegments(self):
        # horizontal - seg1.pt1 - seg2.pt1 - seg1.pt2 - seg2.pt2
        pt1 = Point(0,4); pt2 = Point(4,4); s1 = Segment(pt1,pt2)
        pt3 = Point(-2,4); pt4 = Point(2,4); s2 = Segment(pt3,pt4)
        # vertical - seg1.pt1 - seg2.pt1 - seg2.pt2 - seg1.pt2
        pt5 = Point(4,3); pt6 = Point(4,1); s3 = Segment(pt5,pt6)
        pt7 = Point(4,4); pt8 = Point(4,0); s4 = Segment(pt7,pt8)
        # negative slope - seg1.pt1 - seg2.pt1 - seg1.pt2 - seg2.pt2
        pt9 = Point(0,4); pt10 = Point(4,0); s5 = Segment(pt9,pt10)
        pt11 = Point(-2,6); pt12 = Point(2,2); s6 = Segment(pt11,pt12)
        # positive slope - seg1.pt1 - seg1.pt2 - seg2.pt1 - seg2.pt2
        pt13 = Point(-6,-5); pt14 = Point(-8,-7); s7 = Segment(pt13,pt14)
        pt15 = Point(-12,-11); pt16 = Point(-8,-7); s8 = Segment(pt15,pt16)
        # Collinear to pt1 but they do not intersect
        pt17 = Point(4.1,4); pt18 = Point(4.5,4); s9 = Segment(pt17,pt18)

        # Configure parallel arrays for the loop
        arg1 = [s1, s3, s5, s7, s1]
        arg2 = [s2, s4, s6, s8, s9]
        expectAns = [[Point(0,4), Point(2,4)],
                     [Point(4,3), Point(4,1)],
                     [Point(0,4), Point(2,2)],
                     [Point(-8,-7)],
                     []]

        for i in range(0, len(arg1)):
            res = segmentIntersection.getIntersectionPointsForCollinearSegments(arg1[i], arg2[i])
            res.sort()
            expectAns[i].sort()
            self.assertListEqual(expectAns[i], res)


    def test_orientation(self):
        pt1 = Point(2,2); pt2 = Point(1,1); s1 = Segment(pt1,pt2)
        pt3 = Point(1.4,2) # Clockwise to s1
        pt4 = Point(0.5,0.5) # Collinear to s1
        pt5 = Point(1.5,1) # Counter clockwise to s1

        self.assertEqual(segmentIntersection.orientation(s1,pt3), 1)
        self.assertEqual(segmentIntersection.orientation(s1,pt4), 0)
        self.assertEqual(segmentIntersection.orientation(s1,pt5), -1)


if __name__ == '__main__':
    unittest.main()