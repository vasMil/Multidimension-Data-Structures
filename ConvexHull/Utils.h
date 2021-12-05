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
    double randomDoubleGenerator(int upper, int lower);

    // function that given the number of vertices required
    // will return a vector of pointers to vertices with random x,y.
    // The values of the Vertices created will be in the range defined as [loweri,upperi], where i e {x,y} 
    std::vector<Vertex*> VertexFactory(int numOfVertices, unsigned int upperx, unsigned int lowerx, unsigned int uppery, unsigned int lowery);

    void heapsort(std::vector<Vertex*>* vec, int n);

    void heapify(std::vector<Vertex*>* vec, int n, int i);

    void swap(Vertex* i, Vertex* j);
}