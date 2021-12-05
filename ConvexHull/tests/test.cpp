#include "test.h"

#define TEST_SIZE 500

void test::heapsort() {
    // Create the points to be sorted
    std::vector<Vertex*> randomVertices = Utils::VertexFactory(TEST_SIZE, 100, 90, 10, 0);
    // Sort them using heapsort
    Utils::heapsort(&randomVertices, randomVertices.size());
    // Brute Force test
    for (int i = 0; i < randomVertices.size() - 1; i++) {
        if (randomVertices[i]->getY() > randomVertices[i+1]->getY()) {
            throw std::runtime_error("Heapsort Failed!");
        }
    }
    std::cout << "\nHeapsort test: ok!" << std:: endl;
}