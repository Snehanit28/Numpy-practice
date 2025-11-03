
# BROADCASTING --

# 1. its expands smaller array -> larger array 
# 2. faster than loops 
# 3. use in 1D -> 2D

import numpy as np 

prices = np.array([100,200,300])
discount = 10

final_price = prices - (prices*(discount/100))
print(final_price)     # => [ 90. 180. 270.]



# VECTORIZATION --

# 1. applied in entire array
# 2. 100x faster than loops
# 3. use in matrix operation

import numpy as np 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

result = arr1 + arr2
print(result)         # => [5 7 9]