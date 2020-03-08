#include "headers/blur.h"

using namespace std;

vector < vector <float> > blur(vector < vector < float> > grid, float blurring) {

	int height = grid.size();
	int width = grid[0].size();

	// calculate blur factors
	float center = 1.0 - blurring;
	float corner = blurring / 12.0;
	float adjacent = blurring / 6.0;
  	
  	vector < vector <float> > window = { { corner, adjacent, corner }, { adjacent, center, adjacent }, { corner, adjacent, corner } };

	// variables for blur calculations
	vector <int> DX = { -1, 0, 1 };
	vector <int> DY = { -1, 0, 1 };

	int dx;
	int dy;
  	int i;
  	int j;
	int ii;
	int jj;
	int new_i;
	int new_j;
	float multiplier;
	float val;

	vector < vector <float> > newGrid(height, vector<float>(width, 0.0));

	// blur the grid and store in a new 2D vector
	for (i=0; i< height; i++ ) {
		for (j=0; j<width; j++ ) {
			val = grid[i][j];
			for (ii=0; ii<3; ii++) {
				dy = DY[ii];
				for (jj=0; jj<3; jj++) {
					dx = DX[jj];
					new_i = (i + dy + height) % height;
					new_j = (j + dx + width) % width;
					newGrid[new_i][new_j] += val * window[ii][jj];
				}
			}
		}
	}

	return newGrid;
}
