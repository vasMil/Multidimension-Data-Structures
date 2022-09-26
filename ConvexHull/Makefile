# the compiler: gcc for C program, define as g++ for C++
CC = g++

# compiler flags:
#  -g     - this flag adds debugging information to the executable file
#  -Wall  - this flag is used to turn on most compiler warnings
CFLAGS  = -g -Wall

all: ConvexHull

ConvexHull: ConvexHull.cpp 
			$(CC) $(CFLAGS) -o ConvexHull ConvexHull.cpp Utils.cpp Vertex.cpp tests/test.cpp OpenGL/opengl.cpp -lGL -lglfw

run:
	./ConvexHull

clean:
			rm ConvexHull; clear