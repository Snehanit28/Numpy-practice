import numpy as np

arr_1D = np.array([1,2,3])

arr_2D = np.array([[1,2,3],
       [4,5,6]])

arr_3D = np.array([[[1,2],[3,4],[5,6],[7,8]]])

arr = np.array([10,20,30.5,40])

print(arr_1D.shape)  # => (1, 3)
print(arr_2D.shape)  # => (2,3), here 2 is no of row and 3 is no of coloumn
print(arr_3D.shape)  # => (1, 4, 2)

print(arr_1D.size)   # => 3
print(arr_2D.size)   # => 6, here 6 is total no of elements
print(arr_3D.size)   # => 8

print(arr_1D.ndim)   # => 1
print(arr_2D.ndim)   # => 2, here 2 indicates that it is two dimensional array
print(arr_3D.ndim)   # => 3

print(arr.dtype)     # => float64 its helps to check the data type of the array like int or float

int_arr = arr.astype(int)  # it coverts any data type to another data type
print(int_arr)       # => [10,20,30,40]
print(int_arr.dtype)


