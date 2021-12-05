#include <iostream>

class Vertex {
    private:
        double x;
        double y;
        
    public:
        Vertex(double x, double y);
        void print();

        double getX();
        double getY();
        void updateValues(Vertex v);
};