# TODO : importe numpy sous l'alias np
import numpy as np

# print("Version de NumPy :", np.__version__)
#
# # 1.1 Create a 1D array from the list [1, 2, 3, 4, 5]
# a = np.array([1, 2, 3, 4, 5])
#
# # 1.2 Create a 2D array (3x3) from a list of lists
# b = np.array([ [1, 2, 3], [1, 2, 3], [1, 2, 3]])
#
# # 1.3 Create an array filled with zeros with shape (2, 4)
# zeros_arr = np.zeros((2,4))
#
# # 1.4 Create an array of shape (3, 3) filled with ones.
# ones_arr = np.ones((3,3))
#
# # 1.5 Creates an array containing the integers from 0 to 19 (inclusive) using arange
# range_arr = np.arange(0,20,1)
#
# # 1.6 Create an array of 10 evenly spaced values ​​between 0 and 1 (inclusive) using linspace
# lin_arr = np.linspace(0,1,10)
#
# # 1.7 Create a 4x4 identity matrix
# identity = np.eye(4,4,0)
#
# # 1.8 Create a 3x3 array of random numbers between 0 and 1 (use np.random)
# random_arr = np.random.rand(3,3)
#
# print(a, b, zeros_arr, ones_arr, range_arr, lin_arr, identity, random_arr, sep="\n\n")

m = np.array([[1, 2, 3], [4, 5, 6]])

# 2.1 Displays the shape of m
print("shape :", np.shape(m))

# 2.2 Displays the number of dimensions of m
print("ndim :", np.ndim(m))

# 2.3 Displays the total number of elements in m
print("size :", np.size(m))

# 2.4 Displays the type of elements of m
print("dtype :", m.dtype)

# 2.5 Create a new array identical to m but with float64 elements.
m_float = m.astype(np.float64)

print(m_float.dtype)

