#include "Utils.h"
#include "tests/test.h"

#define NUMBER_OF_POINTS 10

std::vector<Vertex*> convexHull(std::vector<Vertex*> setOfPoints) {
    std::vector<Vertex*> stack;
    Utils::prepareVector(&setOfPoints);

    for (int i = 0; i < NUMBER_OF_POINTS; i++) {
        stack.push_back(setOfPoints[i]);
        if(stack.size() < 3) {
            continue;
        }
        while (stack.size() >= 3 && Utils::isCounterClockwiseTurn(*stack[stack.size()-3], *stack[stack.size()-2], *stack[stack.size()-1]) == -1) {
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
    randomVertices.push_back(new Vertex(9.44693,0.202048));
    randomVertices.push_back(new Vertex(5.4885,0.253926));
    randomVertices.push_back(new Vertex(5.78466,0.667729));
    randomVertices.push_back(new Vertex(3.84022,0.149183));
    randomVertices.push_back(new Vertex(5.59016,2.64943));
    randomVertices.push_back(new Vertex(5.85213,5.40099));
    randomVertices.push_back(new Vertex(4.9771,4.727));
    randomVertices.push_back(new Vertex(4.54326,3.22961));
    randomVertices.push_back(new Vertex(2.52438,8.9872));
    randomVertices.push_back(new Vertex(0.555006,4.93006));

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

    // temp
    for(int i = 0; i < NUMBER_OF_POINTS; i++) {
        std::cout << "(" << randomVertices[i]->getX() << "," << randomVertices[i]->getY() << ")" << std::endl;
    }

    // CLEANUP
    for (int i = 0; i < NUMBER_OF_POINTS; i++) {
        std::cout << i << ". ";
        randomVertices[i]->print();
        delete randomVertices[i];
    }
}