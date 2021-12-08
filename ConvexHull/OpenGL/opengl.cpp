#include "opengl.h"

void opengl::drawStepConvHull(GLFWwindow* window, std::vector<Vertex>* setOfPoints, int numberOfPoints) {
    Utils::prepareVector(setOfPoints);
    std::vector<Vertex*>* stack = new std::vector<Vertex*>();
    for (int i = 0; i < numberOfPoints; i++) {
        opengl::stepConvHull(setOfPoints, stack, &i);
        opengl::drawGraph(window, setOfPoints, stack, 0);

        auto t_ms = std::chrono::time_point_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now());
        std::chrono::milliseconds dt_ms(SLEEP_INTERVAL_IN_MILLI);
        while (t_ms + dt_ms > std::chrono::time_point_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now())) {
            if(glfwWindowShouldClose( window ))
                return;
            glfwPollEvents();
        }
    }
    opengl::drawGraph(window, setOfPoints, stack, 1);
    delete stack;
}

void opengl::stepConvHull(std::vector<Vertex>* setOfPoints, std::vector<Vertex*>* stack, int* iter) {
    if (stack->size() < 3) {
        stack->push_back(&(*setOfPoints)[*iter]);
    }
    else if (Utils::isCounterClockwiseTurn(*(*stack)[stack->size()-3], *(*stack)[stack->size()-2], *(*stack)[stack->size()-1]) == -1) {
        stack->erase(stack->end() - 2);
        (*iter)--;
    }
    else {
        stack->push_back(&(*setOfPoints)[*iter]);
    }
}

GLFWwindow* opengl::initOpenGL() {
    GLFWwindow* window = (GLFWwindow*)malloc(sizeof(GLFWwindow*));
    
    // Initialize the library
    if ( !glfwInit( ) ){
        throw std::runtime_error("Failed to initialize GLFW");
    }
    glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
    window = glfwCreateWindow( SCREEN_WIDTH, SCREEN_HEIGHT, "Convex Hull", NULL, NULL );
    if ( !window ){
        glfwTerminate( );
        throw std::runtime_error("Failed to create a window using GLFW");

    }
    glfwMakeContextCurrent( window );
    glOrtho( -X_AXIS, X_AXIS, -Y_AXIS, Y_AXIS, 0, 1 );
    return window;
}

void opengl::terminateOpenGL(GLFWwindow* window) {
    while ( !glfwWindowShouldClose( window ) ) {
        // Poll for and process events
        glfwPollEvents( );
    }
    glfwTerminate( ); // frees window* aswell
}

void opengl::vec2arrayMapper(std::vector<Vertex>* vec, GLfloat* arr) {
    for (unsigned long int i = 0; i < vec->size(); i++) {
        arr[2*i] = (*vec)[i].getX();
        arr[2*i+1] = (*vec)[i].getY();
    }
}

void opengl::vec2arrayMapper(std::vector<Vertex*>* vec, GLfloat* arr) {
    for (unsigned long int i = 0; i < vec->size(); i++) {
        arr[2*i] = (*vec)[i]->getX();
        arr[2*i+1] = (*vec)[i]->getY();
    }
}

void opengl::drawGraph(GLFWwindow* window, std::vector<Vertex>* vertices, std::vector<Vertex*>* edges, bool isLoop) {
    // Calculate the size of the arrays that you will map into
    int numOfVert = vertices->size();
    int numOfEdges = edges->size();
    // Map vectors to arrays
    GLfloat points[2*numOfVert];
    GLfloat lines[2*numOfEdges];
    opengl::vec2arrayMapper(vertices, points);
    opengl::vec2arrayMapper(edges, lines);

    glClear( GL_COLOR_BUFFER_BIT );

    glEnable( GL_POINT_SMOOTH ); // make the point circular
    glEnableClientState( GL_VERTEX_ARRAY ); // tell OpenGL that you're using a vertex array for fixed-function attribute
    glPointSize( 10 ); // must be added before glDrawArrays is called
    glVertexPointer( 2, GL_FLOAT, 0, points ); // point to the vertices to be used
    glDrawArrays( GL_POINTS, 0, numOfVert ); // draw the vertixes

    glVertexPointer( 2, GL_FLOAT, 0, lines ); // point to the vertices to be used
    isLoop ? glDrawArrays( GL_LINE_LOOP, 0, numOfEdges ) : glDrawArrays( GL_LINE_STRIP, 0, numOfEdges );
    glDisableClientState( GL_VERTEX_ARRAY ); // tell OpenGL that you're finished using the vertex arrayattribute
    glDisable( GL_POINT_SMOOTH ); // stop the smoothing to make the points circular
    glDisableClientState( GL_VERTEX_ARRAY ); // tell OpenGL that you're finished using the vertex arrayattribute

    // Swap front and back buffers
    glfwSwapBuffers( window );
}