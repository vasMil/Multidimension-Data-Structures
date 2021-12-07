#include "Utils.h"
#include "tests/test.h"
#include "OpenGL/opengl.h"

#define NUMBER_OF_POINTS 10

#define X_UPPER_BOUND 20.0
#define X_LOWER_BOUND -20.0
#define Y_UPPER_BOUND 20.0
#define Y_LOWER_BOUND -20.0

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

    // GET POINTS
    std::vector<Vertex*> randomVertices = Utils::VertexFactory(NUMBER_OF_POINTS, X_UPPER_BOUND, X_LOWER_BOUND, Y_UPPER_BOUND, Y_LOWER_BOUND);

    // OpenGL INIT
    GLFWwindow* window = opengl::initOpenGL();

    // CALCULATE THE CONVEX HULL
    std::vector<Vertex*> stack = convexHull(randomVertices);

    opengl::drawGraph(window, &randomVertices, &stack, 1);

    // OpenGL TERMINATE
    opengl::terminateOpenGL(window);

    // CLEANUP
    for (int i = 0; i < NUMBER_OF_POINTS; i++) {
        delete randomVertices[i];
    }
}