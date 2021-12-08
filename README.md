# Multidimension Data Structures
In the scope of the elective course: Multidimension Data Structures, we chose to implement the 3rd project.

## 3D R-trees for Spatio-Temporal Queries in a DB with trajectories on the plane

## Interval trees and Segment Trees

## Convex Hull :heavy_check_mark:
Using the Graham scan algorithm to find the Convex Hull of a random set of vertices. 
- The pseudocode can be found here: https://en.wikipedia.org/wiki/Graham_scan

The result is being displayed using some basic OpenGL functions.
Libraries I installed:
1. OpenGL: sudo apt-get install freeglut3-dev
2. GLFW: sudo apt-get install libglfw3-dev

(Do not forget to point the linker to the installed libraries)

<u>Things that can be improved</u>
- Using `std::list` instread of `std::vector`, since when preparing the vector we essentially remove an element (the one with the smallest y coordinate) and insert it at the beggining of the vector. This requires O(n) time whereas with a doubly linked list could be done in O(1).

## Line Segment Intersection
