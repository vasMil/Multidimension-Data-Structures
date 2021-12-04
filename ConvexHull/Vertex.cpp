#include "Vertex.h"

Vertex::Vertex(double x, double y) {
    this->x = x;
    this->y = y;
}

void Vertex::print() {
    std::cout << "x = " << this->x << "; y = " << this->y << ";\n";
}