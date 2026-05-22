# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# The dimensions have the same size.we check the dimensions from right to left
# OR
# One of the dimensions has a size of 1.
import numpy as np
# Create a 2D row vector
array1 = np.array([[1, 2, 3, 4]])

# Create a 2D column vector
array2 = np.array([[1], [2], [3], [4]])

# Print their shapes
print(array1.shape)
print(array2.shape)

# Multiply them together using broadcasting
print(array1 * array2)


# Create a 2D matrix with shape (2, 4)
array3 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

# Create a 2D column vector with shape (4, 1)
array4 = np.array([[1], [2], [3], [4]])

# Print their shapes
print(array3.shape)
print(array4.shape)

# Attempt to multiply them together using broadcasting
print(array3 * array4) #-->throws error because the first column in the right has value 1 but the second column values don't match and neither of them have values as 1.