import unittest
from model.Point import Point
from model.Segment import Segment
import segmentIntersection

class TestIntersection(unittest.TestCase):

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



if __name__ == '__main__':
    unittest.main()