#include "Utils.h"
#include "tests/test.h"

#define NUMBER_OF_POINTS 5

int main(int argc, char* argv[]) {
    std::cout << "Running Tests!" << std::endl;
    test::heapsort();
    std::cout << "\nTests Finished!\n" << std::endl;


    int i;

    std::vector<Vertex*> randomVertices = Utils::VertexFactory(NUMBER_OF_POINTS, 100, 90, 10, 0);

    for (i = 0; i < NUMBER_OF_POINTS; i++) {
        std::cout << i << ". ";
        randomVertices[i]->print();
    }

    Utils::heapsort(&randomVertices, randomVertices.size());
    std::cout << "\nSize of randomVertices vector: " << randomVertices.size() << '\n' << std::endl;
    
    for (i = 0; i < NUMBER_OF_POINTS; i++) {
        std::cout << i << ". ";
        randomVertices[i]->print();
        free(randomVertices[i]);
    }
}