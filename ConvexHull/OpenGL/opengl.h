#include "../Utils.h"
#include <chrono>
#include <GLFW/glfw3.h>

#define SCREEN_WIDTH 1280
#define SCREEN_HEIGHT 640

#define X_AXIS 20
#define Y_AXIS 20

#define SLEEP_INTERVAL_IN_MILLI 200

namespace opengl {
    GLFWwindow* initOpenGL();
    void terminateOpenGL(GLFWwindow* window);
    void vec2arrayMapper(std::vector<Vertex>* vec, GLfloat* arr);
    void vec2arrayMapper(std::vector<Vertex*>* vec, GLfloat* arr);
    void drawGraph(GLFWwindow* window, std::vector<Vertex> vertices[], std::vector<Vertex*> edges[], bool isLoop);
    void stepConvHull(std::vector<Vertex>* setOfPoints, std::vector<Vertex*>* stack, int* iter);
    void drawStepConvHull(GLFWwindow* window, std::vector<Vertex>* setOfPoints, int numberOfPoints);
}