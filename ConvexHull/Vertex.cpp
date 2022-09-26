#include "Vertex.h"

Vertex::Vertex(double x, double y) {
    this->x = x;
    this->y = y;
}

Vertex::Vertex(std::pair<double, double> p) {
    this->x = p.first;
    this->y = p.second;
}

void Vertex::print() {
    std::cout << "x = " << this->x << "; y = " << this->y << ";\n";
}

double Vertex::getX() {
    return this->x;
}

double Vertex::getY() {
    return this->y;
}

void Vertex::updateValues(Vertex v) {
    this->x = v.x;
    this->y = v.y;
}