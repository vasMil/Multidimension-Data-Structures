#include "Utils.h"
#include "tests/test.h"

#define NUMBER_OF_POINTS 6

std::vector<Vertex*> convexHull(std::vector<Vertex*> setOfPoints) {
    std::vector<Vertex*> stack;
    Utils::prepareVector(&setOfPoints);

    for (int i = 0; i < NUMBER_OF_POINTS; i++) {
        stack.push_back(setOfPoints[i]);
        if(stack.size() < 3) {
            continue;
        }
        if(Utils::isCounterClockwiseTurn(*stack[stack.size()-3], *stack[stack.size()-2], *stack[stack.size()-1]) == -1) {
            Vertex* temp = stack[stack.size() - 1];
            stack.pop_back();
            stack.pop_back();
            stack.push_back(temp);
        }
    }
    return stack;
}

int main(int argc, char* argv[]) {
    // TESTS
    std::cout << "Running Tests!" << std::endl;
    test::heapsort();
    test::isCounterClockwise();
    std::cout << "\nTests Finished!\n" << std::endl;

    // GET POINTS
    // std::vector<Vertex*> randomVertices = Utils::VertexFactory(NUMBER_OF_POINTS, 10, 0, 10, 0);
    std::vector<Vertex*> randomVertices;
    randomVertices.push_back(new Vertex(4.94429, 0.589626));
    randomVertices.push_back(new Vertex(3.89969, 4.1896));
    randomVertices.push_back(new Vertex(2.59867, 4.3064));
    randomVertices.push_back(new Vertex(9.08766, 6.18744));
    randomVertices.push_back(new Vertex(2.02912, 7.82354));
    randomVertices.push_back(new Vertex(9.4, 2.5));

    // PRINT THE POINTS YOU ARE WORKING WITH
    for (int i = 0; i < NUMBER_OF_POINTS; i++) {
        std::cout << i << ". ";
        randomVertices[i]->print();
    }

    // CALCULATE THE CONVEX HULL
    std::vector<Vertex*> stack = convexHull(randomVertices);

    // PRINT VERTICES THAT DEFINE THE CONVEX HULL
    std::cout << "Convex Hull Points: " << std::endl;
    for (long unsigned int i = 0; i < stack.size(); i++) {
        std::cout << i << ". ";
        stack[i]->print();
    }
    std::cout << "End" << std::endl;

    // CLEANUP
    for (int i = 0; i < NUMBER_OF_POINTS; i++) {
        std::cout << i << ". ";
        randomVertices[i]->print();
        delete randomVertices[i];
    }
}