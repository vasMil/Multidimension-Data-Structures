import random
import time
from env.constants import RANGE_OF_POINTS_LIMIT, RANGE_SIZE, NUM_OF_SEGMENTS
from model.Point import Point
from model.Segment import Segment

import sys
import OpenGL.GL as gl
import glfw

import pickle
def saveSegments(segments):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = 'segments/segments_' + timestr + '.txt'
    dbfile = open(filename, 'wb')
    pickle.dump(segments, dbfile)
    dbfile.close()


def getSegments(filename = None):
    if not filename:
        return segmentFactory(-RANGE_OF_POINTS_LIMIT, RANGE_OF_POINTS_LIMIT,
                              -RANGE_OF_POINTS_LIMIT, RANGE_OF_POINTS_LIMIT, NUM_OF_SEGMENTS, 0)
    dbfile = open(filename, 'rb')
    segments = pickle.load(dbfile)
    dbfile.close()

    reInitSegments = []
    for segment in segments:
        reInitSegments.append(Segment(segment.pt1, segment.pt2))
    return reInitSegments


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


def appendIfNotInList(list, data):
    if data in list:
        return
    list.append(data)


def drawResults(segments, intersectionPoints, windowTitle):
    def on_key(window, key, scancode, action, mods):
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window,1)

    # Initialize the library
    if not glfw.init():
        sys.exit()

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(2560, 1700, windowTitle, None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    # Make the window's context current
    glfw.make_context_current(window)

    # Install a key handler
    glfw.set_key_callback(window, on_key)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here
        width, height = glfw.get_framebuffer_size(window)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glColor3f(1.0, 1.0, 1.0)
        gl.glLineWidth(5.0)
        gl.glEnable(gl.GL_BLEND)
        gl.glBegin(gl.GL_LINES)
        for segment in segments:
            gl.glVertex2f(segment.pt1.x/RANGE_SIZE, segment.pt1.y/RANGE_SIZE)
            gl.glVertex2f(segment.pt2.x/RANGE_SIZE, segment.pt2.y/RANGE_SIZE)
        gl.glEnd()

        gl.glPointSize(15.0)
        gl.glColor3f(1.0, 0.2, .18)
        gl.glEnable(gl.GL_BLEND)

        gl.glBegin(gl.GL_POINTS)
        for point in intersectionPoints:
            gl.glVertex2f(point.x/RANGE_SIZE,point.y/RANGE_SIZE)
        gl.glEnd()

        gl.glFlush()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()