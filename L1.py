import numpy as np

# Creating Arrays from python list

arr = np.array([1,2,3,4])

print(arr)  # => [1 2 3 4]

# Creating Arrays from python list with default values

zeros_array = np.zeros(3)  # its fills array with zeros
print(zeros_array)  # => [0. 0. 0.]

ones_array = np.ones((2,3))  # its fills array with ones
print(ones_array)   # =>[[1. 1. 1.] in next line [1. 1. 1.]]

#Creating Arrays from python list with full function

filled_array = np.full((3,3),6)  # its fills array with some value here (3,3) is shape and 6 is value
print(filled_array)   # =>[[6 6 6] in next line [6 6 6] and in next line [6 6 6]]


#Creating sequences of numbers in numpy
# arange(start,stop,step)
arr_1 = np.arange(1,12,3)
print(arr_1)  # => [1 4 7 10] ,1+3=4, 4+3=7, 7+3=10


#Creating identify matrix 
# eye(size)
identify_matrix = np.eye(3)
print(identify_matrix)  # =>[[1. 0. 0.] in next line [0. 1. 0.] in next line [0. 0. 1.]]