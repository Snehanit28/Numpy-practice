import numpy as np


#  RESHAPE

#reshape(row,columns) specify new shape if dimensions match

arr = np.array([1,2,3,4,5,6])

reshape_Arr = arr.reshape(2,3)
print(reshape_Arr)               # =>[[1 2 3] in next line [4,5,6]]  
                          
#reshaping does not create a copy it returns a view


#  FLATTENING ARRAYS

#.ravel()  returns a view
#.flatten()  returns a copy

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())    # => [1 2 3 4 5 6]
print(arr_2d.flatten())    # => [1 2 3 4 5 6]