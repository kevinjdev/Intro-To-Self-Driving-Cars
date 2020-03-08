#include "headers/normalize.h"
using namespace std;

vector< vector<float> > normalize(vector< vector <float> > grid) {

	float total = 0.0;

	for (int i = 0; i < grid.size(); i++)
	{
		for (int j=0; j < grid[0].size(); j++)
		{
			total += grid[i][j];
		}
	}

	for (int i = 0; i < grid.size(); i++) {
		for (int j=0; j < grid[0].size(); j++) {
			grid[i][j] = grid[i][j] / total;
		}
	}

	return grid;
}
