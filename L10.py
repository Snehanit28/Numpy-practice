# Built in function 1

import numpy as np
arr = np.array([1, 2, np.nan, 4, np.nan, 6])


# np.isnan(array)

print(np.isnan(arr))    # => [False False  True False  True False]


# np.nan_to_num(array, nan = value)

cleaned_arr = np.nan_to_num(arr, nan = 3)    
print(cleaned_arr)      # => [1. 2. 3. 4. 3. 6.]