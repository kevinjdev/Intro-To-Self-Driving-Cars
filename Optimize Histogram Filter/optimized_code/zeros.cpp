#include "headers/zeros.h"

using namespace std;

// Return a zeros vector with int height and int width
vector < vector <float> > zeros(int height, int width) {
	return vector < vector <float> >(height, vector<float>(width, 0.0));
}