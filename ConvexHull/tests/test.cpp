#include "test.h"

#define TEST_SIZE 250

void test::isCounterClockwise() {
    // Create points
    Vertex v1(1,1);
    Vertex v2(4,2);
    Vertex v3(1,3);
    Vertex v4(1,-1);

    if (Utils::isCounterClockwiseTurn(v2, v1, v3) != -1)
        throw std::runtime_error("isCounterClockwiseTurn Failed on detecting a clockwise turn");

    if (Utils::isCounterClockwiseTurn(v3, v1, v2) != 1)
        throw std::runtime_error("isCounterClockwiseTurn Failed on detecting a counter clockwise turn");

    if (Utils::isCounterClockwiseTurn(v3, v1, v4) != 0)
        throw std::runtime_error("isCounterClockwiseTurn Failed on detecting collinear points");

    std::cout << "\nisCounterClockwiseTurn test: ok!" << std:: endl;
}


void test::heapsort() {
    // Create the points to be sorted
    std::vector<Vertex>* randomVertices = Utils::VertexFactory(TEST_SIZE, 100, 90, 10, 0);
    // Create a vec that has the exact same y coord as randomVertices
    // but all the x coordinates are incremented by one
    std::vector<Vertex>* vec = new std::vector<Vertex>();
    for (long unsigned int i = 0; i < randomVertices->size(); i++) {
        vec->push_back(Vertex((*randomVertices)[i].getX()+1, (*randomVertices)[i].getY()));
    }
    // Combine the two vectors
    randomVertices->insert(randomVertices->end(), vec->begin(), vec->end());
    // Sort them using heapsort, but element at pos 0 be the one with the min-y coord
    Utils::prepareVector(randomVertices);
    Vertex miny = (*randomVertices)[0];
    // Brute Force test
    for (long unsigned int i = 0; i < randomVertices->size() - 1; i++) {
        if (Utils::isCounterClockwiseTurn(miny, (*randomVertices)[i], (*randomVertices)[i+1]) == -1) {
            free(randomVertices);
            throw std::runtime_error("Heapsort Failed!");
        }
        else if (Utils::isCounterClockwiseTurn(miny, (*randomVertices)[i], (*randomVertices)[i+1]) == 0 && (*randomVertices)[i].getX() > (*randomVertices)[i+1].getX()) {
            free(randomVertices);
            throw std::runtime_error("Heapsort Failed on x-coordinate!");
        }
    }
    std::cout << "\nHeapsort test: ok!" << std:: endl;

    // Cleanup
    free(randomVertices);
    delete vec;
}