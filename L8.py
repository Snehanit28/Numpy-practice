# STACKING & SPLITING


import numpy as np

# STACKING

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1,arr2)))    # => verticallay stack    => [[1 2 3] in next line [4 5 6]]
print(np.hstack((arr1,arr2)))    # => horizontally stack   => [1 2 3 4 5 6]

# SPLITING

arr = np.array([10,20,30,40,50,60])
print(np.split(arr,2))   # => [array([10, 20, 30]), array([40, 50, 60])]