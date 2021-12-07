#pragma once
#include <stdlib.h>
#include <vector>
#include <string>
#include <random>
#include <functional>
#include <iostream>
#include <fstream>
#include "Vertex.h"

namespace Utils {
    double randomDoubleGenerator(double upper, double lower);

    // function that given the number of vertices required
    // will return a vector of pointers to vertices with random x,y.
    // The values of the Vertices created will be in the range defined as [loweri,upperi], where i e {x,y} 
    std::vector<Vertex*> VertexFactory(int numOfVertices, double upperx, double lowerx, double uppery, double lowery);

    void heapsort(std::vector<Vertex*>* vec, int n, Vertex* miny);

    void heapify(std::vector<Vertex*>* vec, int n, int i, Vertex* miny);

    void swap(Vertex* i, Vertex* j);

    // 0 -> Colinear | 1 -> Counter Clockwise | -1 -> Clockwise
    int isCounterClockwiseTurn(Vertex v1, Vertex v2, Vertex v3);

    // Return the index of the Vertex with min-y in vec (if more than one have the same min-y coord, it picks the one with the min-x)
    // uses brute force O(n)
    int getMinYVertex(std::vector<Vertex*>* vec);

    // Given a vector of vertices, it finds the Vertix with the min-y coordinate (O(n))
    // Removes it from that vector (worst case O(n) -> https://stackoverflow.com/questions/28266382/time-complexity-of-removing-items-in-vectors-and-deque)
    // Sorts the rest of the elements based on the angle of the line defined by each point and the 
    // vertex with min-y, using heapsort. (O(nlogn))
    // Inserts the vertex removed at step 1 at the beggining of the vector. (O(n))
    // TODO: Consider refactoring the code so you are using a double-linked list
    void prepareVector(std::vector<Vertex*>* vec);
}