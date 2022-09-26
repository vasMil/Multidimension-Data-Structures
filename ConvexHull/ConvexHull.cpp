#include "Utils.h"
#include "tests/test.h"
#include "OpenGL/opengl.h"

#define TEST 0
#define DRAW 1
#define DRAW_STEPS 1

#define NUMBER_OF_POINTS 100

#define X_UPPER_BOUND 20.0
#define X_LOWER_BOUND -20.0
#define Y_UPPER_BOUND 20.0
#define Y_LOWER_BOUND -20.0

std::vector<Vertex*>* convexHull(std::vector<Vertex>* setOfPoints) {
    std::vector<Vertex*>* stack = new std::vector<Vertex*>();
    Utils::prepareVector(setOfPoints);

    for (int i = 0; i < NUMBER_OF_POINTS; i++) {
        stack->push_back(&(*setOfPoints)[i]);
        if(stack->size() < 3) {
            continue;
        }
        while (stack->size() >= 3 && Utils::isCounterClockwiseTurn(*(*stack)[stack->size()-3], *(*stack)[stack->size()-2], *(*stack)[stack->size()-1]) == -1) {
            stack->erase(stack->end() - 2);
        }
    }
    return stack;
}

int main(int argc, char* argv[]) {
#if TEST
    std::cout << "Running Tests!" << std::endl;
    test::heapsort();
    test::isCounterClockwise();
    std::cout << "\nTests Finished!\n" << std::endl;
#endif

#if !TEST
    // GET POINTS
    std::vector<Vertex>* randomVertices = Utils::VertexFactory(NUMBER_OF_POINTS, X_UPPER_BOUND, X_LOWER_BOUND, Y_UPPER_BOUND, Y_LOWER_BOUND);

#if DRAW || DRAW_STEPS
    // OpenGL INIT
    GLFWwindow* window = opengl::initOpenGL();
#endif

    // CALCULATE THE CONVEX HULL
    std::vector<Vertex*>* stack = convexHull(randomVertices);

    // DRAW
#if DRAW && !DRAW_STEPS
    opengl::drawGraph(window, randomVertices, stack, 1);
#elif DRAW_STEPS
    opengl::drawStepConvHull(window, randomVertices, NUMBER_OF_POINTS);
#endif

#if DRAW || DRAW_STEPS
    // OpenGL TERMINATE
    opengl::drawGraph(window, randomVertices, stack, 1);
    opengl::terminateOpenGL(window);
#endif

    // CLEANUP
    delete stack; // The pointers that it holds point to randomVertices vector
    free(randomVertices);
#endif
}