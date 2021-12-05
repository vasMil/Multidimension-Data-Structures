#include "test.h"

#define TEST_SIZE 250

void test::heapsort() {
    // Create the points to be sorted
    std::vector<Vertex*> randomVertices = Utils::VertexFactory(TEST_SIZE, 100, 90, 10, 0);
    // Create a vec that has the exact same y coord as randomVertices
    // but all the x coordinates are incremented by one
    std::vector<Vertex*> vec;
    for (int i = 0; i < randomVertices.size(); i++) {
        vec.push_back(new Vertex(randomVertices[i]->getX()+1, randomVertices[i]->getY()));
    }
    // Combine the two vectors
    randomVertices.insert(randomVertices.end(), vec.begin(), vec.end());
    // Sort them using heapsort
    Utils::heapsort(&randomVertices, randomVertices.size());
    // Brute Force test
    for (int i = 0; i < randomVertices.size() - 1; i++) {
        if (randomVertices[i]->getY() > randomVertices[i+1]->getY()) {
            throw std::runtime_error("Heapsort Failed!");
        }
        else if (randomVertices[i]->getY() == randomVertices[i+1]->getY() && randomVertices[i]->getX() < randomVertices[i+1]->getX()) {
            std::cout << "rip" << std::endl;
            throw std::runtime_error("Heapsort Failed on x-coordinate!");
        }
    }
    std::cout << "\nHeapsort test: ok!" << std:: endl;

    for (int i = 0; i < randomVertices.size(); i++) {
        // std::cout << i << ". ";
        // randomVertices[i]->print();
        free(randomVertices[i]);
    }
}