#include "Utils.h"

void Utils::prepareVector(std::vector<Vertex*>* vec) {
    int miny_index = Utils::getMinYVertex(vec);
    Vertex* miny = (*vec)[miny_index];
    vec->erase(vec->begin() + miny_index);
    Utils::heapsort(vec, vec->size(), miny);
    vec->insert(vec->begin(), miny);
}

int Utils::isCounterClockwiseTurn(Vertex v1, Vertex v2, Vertex v3) {
    double outter = (v2.getX() - v1.getX())*(v3.getY() - v1.getY()) - (v3.getX() - v1.getX())*(v2.getY() - v1.getY());
    if (outter == 0) return 0;
    return outter > 0 ? 1 : -1;
}

void Utils::heapsort(std::vector<Vertex*>* vec, int n, Vertex* miny) {
    int i = 0;
    for (i = n/2 -1; i >= 0; i--) {
        Utils::heapify(vec, n, i, miny);
    }

    for (int i = n - 1; i > 0; i--) {
        // Move current root to end
        swap((*vec)[0], (*vec)[i]);

        // call max heapify on the reduced heap
        Utils::heapify(vec, i, 0, miny);
    }
}

void Utils::heapify(std::vector<Vertex*>* vec, int n, int i, Vertex* miny) {
    int i_largest = i;
    int left_child = 2*i_largest + 1;
    int right_child = 2*i_largest + 2;

    if (left_child < n && Utils::isCounterClockwiseTurn(*miny, *(*vec)[i_largest], *(*vec)[left_child]) == 1) {
        i_largest = left_child;
    }
    else if (left_child < n && Utils::isCounterClockwiseTurn(*miny, *(*vec)[i_largest], *(*vec)[left_child]) == 0 && (*vec)[i_largest]->getX() < (*vec)[left_child]->getX()) {
        i_largest = left_child;
    }

    if (right_child < n && Utils::isCounterClockwiseTurn(*miny, *(*vec)[i_largest], *(*vec)[right_child]) == 1) {
        i_largest = right_child;
    }
    else if (right_child < n && Utils::isCounterClockwiseTurn(*miny, *(*vec)[i_largest], *(*vec)[right_child]) == 0 && (*vec)[i_largest]->getX() < (*vec)[right_child]->getX()) {
        i_largest = right_child;
    }

    if (i_largest != i) {
        Utils::swap((*vec)[i_largest], (*vec)[i]);
        heapify(vec, n, i_largest, miny);
    }

}


void Utils::swap(Vertex* i, Vertex* j) {
    Vertex temp = *i;
    i->updateValues(*j);
    j->updateValues(temp);
}

int Utils::getMinYVertex(std::vector<Vertex*>* vec) {
    int miny = 0;
    for(long unsigned int i = 1; i < vec->size(); i++) {
        if((*vec)[miny]->getY() > (*vec)[i]->getY()) {
            miny = i;
        }
        else if ((*vec)[miny]->getY() == (*vec)[i]->getY() && (*vec)[miny]->getX() > (*vec)[i]->getX()) {
            miny = i;
        }
    }
    return miny;
}

std::vector<Vertex*> Utils::VertexFactory(int numOfVertices, double upperx, double lowerx, double uppery, double lowery) {
    std::vector<Vertex*> randomVertices(numOfVertices);
    for (int i = 0; i < numOfVertices; i++) {
        randomVertices[i] = new Vertex(Utils::randomDoubleGenerator(upperx, lowerx), Utils::randomDoubleGenerator(uppery, lowery));
    }
    return randomVertices;
}


double Utils::randomDoubleGenerator(double upper, double lower) {
    uint32_t seed_val = 0; // Declare value to store data into
    size_t size = sizeof(seed_val); // Declare size of data
    
    std::fstream urandom;
    urandom.open("/dev/urandom", std::ios::in | std::ios::binary); // Open stream
    if(urandom) // Check if stream is open
    {
        // seed_val address being casted as a char* (character array), so I may use read to store bytes in that array.
        urandom.read(reinterpret_cast<char*>(&seed_val), size); // Read from urandom
        if(!urandom) // Check if read failed
        {
            throw std::runtime_error("Couldn't read from /dev/urandom");
        }
        urandom.close(); // close stream
    }
    else // Open failed
    {
        throw std::runtime_error("Failed to open /dev/urandom");
    }

    
    std::mt19937 engine; // Mersenne twister MT19937
    engine.seed(seed_val);
    std::uniform_real_distribution<double> distribution(upper, lower);
    
    double random = distribution(engine); // Generate sample directly using the distribution and the engine objects.
    return random;
}