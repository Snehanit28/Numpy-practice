import numpy as np

arr = np.array([10,20,30,40,50,60])

#  INDEXING

print(arr[0])        # => 10
print(arr[2])        # => 30
print(arr[-1])       # => 60


# SLICING

#arr[start:end]   #(start to end-1) 
#arr[start:end:step] 

print(arr[1:5])   #index 1 to 4    # => [20 30 40 50]
print(arr[:4])    #index 0 to 3    # => [10 20 30 40]
print(arr[::2])   #every second element     # => [10 30 50]
print(arr[::-1])  #reverse the array        # => [60 50 40 30 20 10]
print(arr[2::2])  # => [30 50]



# FANCY INDEXING

print(arr[[0,3,5]])  # => [10 40 60]



# BOLLEAN MASKING or FILTERING

print(arr[arr<25]) # => [10 20] prints the numers which are less than 25 in the array