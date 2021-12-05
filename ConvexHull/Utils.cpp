#include "Utils.h"

void Utils::heapsort(std::vector<Vertex*>* vec, int n) {
    int i = 0;
    for (i = n/2 -1; i >= 0; i--) {
        Utils::heapify(vec, n, i);
    }

    for (int i = n - 1; i > 0; i--) {
        // Move current root to end
        swap((*vec)[0], (*vec)[i]);

        // call min heapify on the reduced heap
        Utils::heapify(vec, i, 0);
    }
}

void Utils::heapify(std::vector<Vertex*>* vec, int n, int i) {
    int i_smallest = i;
    int left_child = 2*i_smallest + 1;
    int right_child = 2*i_smallest + 2;

    if (left_child < n && (*vec)[left_child]->getY() > (*vec)[i_smallest]->getY()) {
        i_smallest = left_child;
    }

    if (right_child < n && (*vec)[right_child]->getY() > (*vec)[i_smallest]->getY()) {
        i_smallest = right_child;
    }

    if (i_smallest != i) {
        Utils::swap((*vec)[i_smallest], (*vec)[i]);
        heapify(vec, n, i_smallest);
    }

}


void Utils::swap(Vertex* i, Vertex* j) {
    Vertex temp = *i;
    i->updateValues(*j);
    j->updateValues(temp);
}

std::vector<Vertex*> Utils::VertexFactory(int numOfVertices, unsigned int upperx, unsigned int lowerx, unsigned int uppery, unsigned int lowery) {
    std::vector<Vertex*> randomVertices(numOfVertices);
    for (int i = 0; i < numOfVertices; i++) {
        randomVertices[i] = new Vertex(Utils::randomDoubleGenerator(upperx, lowerx), Utils::randomDoubleGenerator(uppery, lowery));
    }
    return randomVertices;
}


double Utils::randomDoubleGenerator(int upper, int lower) {
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