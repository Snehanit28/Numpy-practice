import numpy as np

#  CONCATENATE

# np.concatenate((array1,array2,axis=0))

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr = np.concatenate((arr1,arr2))

print(new_arr)      # => [1 2 3 4 5 6]



# DELETE


arr = np.array([10,20,30,40,50,60])
new_arr = np.delete(arr,0)
print(new_arr)    # => [20 30 40 50 60]

arr_2d = np.array([[1,2,3],[4,5,6]])
new_arr_2d = np.delete(arr_2d,0,axis=0)
print(new_arr_2d)    # => [[4 5 6]]