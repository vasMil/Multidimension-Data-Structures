#include <iostream>
#include <vector>
#include "Utils.h"

#define NUMBER_OF_POINTS 100

int main(int argc, char* argv[]) {
    std::vector<Vertex*> randomVertices = Utils::VertexFactory(NUMBER_OF_POINTS, 100, 90, 10, 0);

    for (int i = 0; i < NUMBER_OF_POINTS; i++) {
        std::cout << i << ". ";
        randomVertices[i]->print();
        free(randomVertices[i]);
    }
}