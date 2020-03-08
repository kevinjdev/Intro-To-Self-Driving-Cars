# Udacity-Intro-Self-Driving-Cars
Completed Projects from Udacity's Intro to Self Driving Cars Nanodegree
## Getting Started
Clone the repository to your local machine by running the following command in a terminal window or command prompt from the location you wish to copy the folder

`git clone https://github.com/kevinjdev/Udacity-Intro-Self-Driving-Cars.git`

## Histogram Filter in Python2
For this project I implemented the 2D **sense** function in *localize.py* to update a robot's belief in its current position to perform localization. I also used pdb to debug the **move** function, fixing a bug due  to incorrect array indexing.

### Prerequisites
* Jupyter Notebook installed
* Python 2 environment active. Using Anaconda, I ran the following 2 commands in terminal to set up a python2 environment in Jupyter
```
conda install nb_conda_kernels
conda create -n py27 python=2.7 ipykernel
```
### How To Run
Start Jupyter, then open the notebook file **writeup.ipynb** located in the **Histogram Filter in Python2** folder. Each section of code can be run by pressing *ctrl+enter*.

## Implement a Matrix Class
For this project I implemented the following functions in *matrix.py*
```
class Matrix:
  def determinant(self):
      # your code

  def trace(self):
      # your code

  def inverse(self):
      # your code

  def transpose(self):
     # your code

  # Overloaded operators

  def __add__(self,other):
    # your code

  def __sub__(self,other):
    # your code

  def __mul__(self,other):
    # your code
```
The **matrix_playground.ipynb** notebook tests the *matrix.py* class. The **kalman_filter_demo.ipynb** has a demo of a kalman filter that works once the *matrix.py* class is implemented correctly.

### How To Run
Start Jupyter, then open the notebook file **matrix_playground.ipynb** located in the **Implement a Matrix Class** folder. This is a python 3 project. Each section of code can be run by pressing *ctrl+enter*.

## Translate Python to C++
This project involved converting the **Histogram Filter in Python** written in the dynamically typed language Python to the statically typed language C++. I implemented the following functions:

`normalize() and blur() in helpers.cpp`

`initialize_beliefs(), sense(), and move() in *localizer.cpp*`

### How to Run
`g++ -std=c++11 tests.cpp`

`./a.out`

## Optimize Histogram Filter
This project involved optimizing the following files: 
```
zeros.cpp
initialize_beliefs.cpp
sense.cpp
blur.cpp
normalize.cpp
move.cpp
```
Optimization techniques utilized:
- reserving memory for vectors
- passing larger variables to functions by reference
- removing variables that were not needed
- modifying vectors in place when possible instead of creating new vector variables
- removing dead code (lines of code that were in the files but no longer being used)
- avoiding extra for loops especially nested for loops when possible
- avoiding extra if statements
- using static and const keywords when appropriate
- compiling with the -O3 (letter O)

### How to Run
In the folder **Optimize Histogram Filter/optimized_code** run the commands below. To compare to un-optimized code, the same command can be run in the folder **andy_histogram_filter**. Add the compiler flag -O3 to achieve the fastest run time.

`g++ -std=c++11 main.cpp blur.cpp initialize_beliefs.cpp move.cpp normalize.cpp print.cpp sense.cpp zeros.cpp`

`./a.out`

## Implement Route Planner
In this project, I implemented parts of an A* search algorithm to plan the shortest route between two nodes.

### How to Run
Start Jupyter, then in the folder **Implement Route Planner** open the **project_notebook.ipynb**. Each section of code can be run by pressing *ctrl+enter*.

