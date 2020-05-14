# Udacity-Intro-Self-Driving-Cars
Completed Projects from Udacity's Intro to Self Driving Cars Nanodegree
## Getting Started
Clone the repository to your local machine by running the following command in a terminal window or command prompt from the location you wish to copy the folder

`git clone https://github.com/kevinjdev/Udacity-Intro-Self-Driving-Cars.git`

## Prerequisites
* For the Python projects, Jupyter Notebook should be installed
* For the C++ projects, a gcc compiler should be installed.

## Histogram Filter in Python2 && Histogram Filter in Python3
I implemented the 2D **sense** function in *localize.py* to update a robot's belief in its current position to perform localization. I also used pdb to debug the **move** function, fixing a bug due  to incorrect array indexing.

### Known Issue
* To run **Histogram Filter in Python2**, a Python 2 environment needs to be active. Python 2 is no longer supported as of April 2020, so I have modified this project for Python 3 under the title **Histogram Filter in Python3**. Using Anaconda, I ran the following 2 commands in terminal to set up a Python 2 environment in Jupyter. All other Python projects use Python 3. 
```
conda install nb_conda_kernels
conda create -n py27 python=2.7 ipykernel
```
### How To Run
Start Jupyter, then open the notebook file **writeup.ipynb** located in the **Histogram Filter in Python2** folder. Each section of code can be run by pressing *ctrl+enter*.

The same instructions apply to run the project **Histogram Filter in Python3**. Choose the Python3 kernel in Jupyter notebook if not already selected.

## Implement a Matrix Class
I implemented the following functions in *matrix.py*
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
Start Jupyter, then in the folder **Implement a Matrix Class** open the notebook **matrix_playground.ipynb**. Each section of code can be run by pressing *ctrl+enter*.

## Translate Python to C++
I converted the **Histogram Filter in Python** written in the dynamically typed language Python to the statically typed language C++. I implemented the following functions:

`normalize() and blur() in helpers.cpp`

`initialize_beliefs(), sense(), and move() in *localizer.cpp*`

### How to Run
`g++ -std=c++11 tests.cpp`

`./a.out`

## Optimize Histogram Filter
I optimized the C++ code in the following files: 
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
I implemented parts of an A* search algorithm to plan the shortest route between two nodes.

### How to Run
Start Jupyter, then in the folder **Implement Route Planner** open the notebook **project_notebook.ipynb**. Each section of code can be run by pressing *ctrl+enter*.

## Reconstructing Trajectories from Sensor Data
I integrated accelerometer(acceleration) data to obtain speeds, and integrated gyrometer(yaw rate) data to obtain headings then plotted the data using matplotlib. Integration is performed by calculating area under the curve with time on the x axis. Algebraic integration techniques are not used.

### How to Run
Start Jupyter, then in the folder **Reconstructing Trajectories from Sensor Data** open the notebook **Reconstructing Trajectories.ipynb**. Each section of code can be run by pressing *ctrl+enter*.

### Known Issue
There are some deprecation issues with plotly and so the graphs don't display correctly. I updated the plotly import in helpers.py to be `import chart_studio.plotly as py`. There are a few other issues related to this I still need to fix.

To install plotly and chart studio:

`conda install -c plotly plotly=4.5.2`

`conda install -c plotly chart-studio=1.0.0`

## Traffic Light Classifier
I built a image classifer that performs the classifies a traffic light image as being a red, yellow, or green light. The recipe for classifying the images is below.
- Loading and visualizing the data.
- Pre-processing. 
- Feature extraction. 
- Classification and visualizing error.
- Evaluate the model.

I achieved accuracy of 0.9730639730639731 with the brightness feature extraction that I implemented.
```
def brightness_feature(rgb_image):

    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    
    # Create a mask for red, yellow, and green
    [maskR, maskY, maskG] = create_masks(hsv_image)
    
    # Apply each mask individually to image before determining brightness
    hsv_mask_imgR = cv2.bitwise_and(rgb_image, rgb_image, mask=maskR)
    hsv_mask_imgG = cv2.bitwise_and(rgb_image, rgb_image, mask=maskG)
    hsv_mask_imgY = cv2.bitwise_and(rgb_image, rgb_image, mask=maskY)
    
    # Calculate brightness using each mask and summing over the 1/3 of image corresponding
    # to location where respective color should appear.
    brightness = {}
    brightness["yellow"] = np.sum(hsv_mask_imgY[11:21, :, 2]) # sum over middle 1/3
    brightness["red"] = np.sum(hsv_mask_imgR[:11,:,2]) # sum over top 1/3
    brightness["green"] = np.sum(hsv_mask_imgG[21:,:,2]) #sum over bottom 1/3
    
    # Returns the label with the max brightness. If all 3 brightness values are zero (mask filtered out all colors) 
    # then yellow will be returned.
    return max(brightness, key = lambda k: brightness[k])
```
### Known Issue
OpenCV must be installed to run 

To install using conda:

`conda install opencv`

### How to Run

Start Jupyter, then in the folder **Traffic Light Classifer** open the notebook **Traffic_Light_Classifier.ipynb**. Each section of code can be run by pressing *ctrl+enter*.
