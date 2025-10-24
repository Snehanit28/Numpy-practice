import numpy as np

# Operators

arr = np.array([10,20,30,40])

print(arr+2)  # => [12 22 32 42]
print(arr-1)  # => [ 9 19 29 39]
print(arr*3)  # => [ 30  60  90 120]
print(arr/2)  # => [ 5. 10. 15. 20.]
print(arr**2) # => [ 100  400  900 1600]
print(arr//2) # => [ 5 10 15 20]
print(arr%3)  # => [1 2 0 1]


# Agriggation function

print(np.sum(arr))   # => 100
print(np.mean(arr))  # => 25.0
print(np.min(arr))   # => 10
print(np.max(arr))   # => 40 
print(np.std(arr))   # => 11.180339887498949
print(np.var(arr))   # => 125.0
