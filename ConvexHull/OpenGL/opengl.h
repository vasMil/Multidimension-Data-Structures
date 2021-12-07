#include "../Utils.h"
#include <unistd.h>
#include <GL/glew.h>
#include <GLFW/glfw3.h>

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480

#define X_AXIS 20
#define Y_AXIS 20

#define SLEEP_INTERVAL_IN_MICRO 500000

namespace opengl {
    GLFWwindow* initOpenGL();
    void terminateOpenGL(GLFWwindow* window);
    void vec2arrayMapper(std::vector<Vertex>* vec, GLfloat* arr);
    void vec2arrayMapper(std::vector<Vertex*>* vec, GLfloat* arr);
    void drawGraph(GLFWwindow* window, std::vector<Vertex> vertices[], std::vector<Vertex*> edges[], bool isLoop);
}