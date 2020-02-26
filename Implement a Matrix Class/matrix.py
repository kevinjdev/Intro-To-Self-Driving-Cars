import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
    
    def dot_product(self, v1, v2):
        """
        Returns the sum of multiplying 2 vectors
        """
        if len(v1) != len(v2):
            raise(ValueError, "Dimensions don't match for dot product calculation")
            
        result = 0
        for i in range(len(v1)):
            result += v1[i] * v2[i]
        
        return result
            
            
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # matrix is 1x1
        if self.h == 1:
            return self.g[0][0]
        
        # matrix is 2x2. return (ad - bc)
        return self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        result = 0
        for i in range(self.h):
            result += self.g[i][i]
        
        return result
        

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        if self.determinant() == 0:
            raise(ValueError, "Matrix with determinant of 0 does not have an inverse")
        
        # 1x1 matrix
        if self.h == 1:
            g = [[1 / self.g[0][0]]]
            
            return Matrix(g)
        
        # 2x2 matrix
        I = identity(2)
        tr = self.trace()
        
        return 1 / self.determinant() * ((tr * I) - self)    
        
            
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        for i in range(self.w):
            column = []
            for j in range(self.h):
                column.append(self.g[j][i])
            matrix_transpose.append(column)

        return Matrix(matrix_transpose)
            
                
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling 
        on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        result = []
        for row in range(self.h):
            result_row = []
            for col in range(self.w):
                result_row.append(self.g[row][col] + other.g[row][col])
            result.append(result_row)
        
        return Matrix(result)
                           

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        result = []
        for row in range(self.h):
            result_row = []
            for col in range(self.w):
                result_row.append(-1.0 * self.g[row][col])
            result.append(result_row)
        
        return Matrix(result)
                
                
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subracted if the dimensions are the same")
        
        result = []
        for row in range(self.h):
            result_row = []
            for col in range(self.w):
                result_row.append(self.g[row][col] - other.g[row][col])
            result.append(result_row)
        
        return Matrix(result)
    
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise(ValueError, "Dimensions don't match for matrix multiplication")
       
        other_transpose = other.T()
        result =[]
        for i in range(self.h):
            result_row = []
            for j in range(other_transpose.h):
                dp = self.dot_product(self.g[i], other_transpose.g[j])
                result_row.append(dp)
            result.append(result_row)       
        
        return Matrix(result)
                                 

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
        
        result = []
        for row in range(self.h):
            result_row = []
            for col in range(self.w):
                result_row.append(self.g[row][col] * other)
            result.append(result_row)
        
        return Matrix(result)
            