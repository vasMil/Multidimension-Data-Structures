from utils import segmentFactory

segments = segmentFactory(0,100,0,100,50)
for i in range(0,len(segments)):
    segments[i].print()