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
Start Jupyter, then open the notebook file **writeup.ipynb** located in the **Histogram Filter in Python2** folder

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
The **matrix_playground.ipynb** notebook tests the *matrix.py* class. the **kalman_filter_demo.ipynb** has a demo of an implemented kalman filter that works once the *matrix.py* class is implemented correctly.

### How To Run
Start Jupyter, then open the notebook file **matrix_playground.ipynb** located in the **Implement a Matrix Class** folder. This is a python 3 project.
