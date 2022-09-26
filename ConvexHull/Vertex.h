#include <iostream>

class Vertex {
    private:
        double x;
        double y;
        
    public:
        Vertex(double x, double y);
        Vertex(std::pair<double, double> p);
        void print();

        double getX();
        double getY();
        void updateValues(Vertex v);
};