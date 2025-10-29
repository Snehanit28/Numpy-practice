import numpy as np 

# np.insert(array,index,value,axis=none) 

arr = np.array([10,20,30,40,50])
new_arr = np.insert(arr,2,100)
print(new_arr)       # => [ 10  20 100  30  40  50]

arr_2d = np.array([[1,2],[3,4]])

arr_2d_1 = np.insert(arr_2d,1,[5,6],axis=0)
print(arr_2d_1)   # [[1 2] in next line [5 6] in next line [3 4]]

arr_2d_2 = np.insert(arr_2d,1,[5,6],axis=1)
print(arr_2d_2)   # [[1 5 2] in next line [3 6 4]]

arr_2d_3 = np.insert(arr_2d,1,[5,6],axis=None)
print(arr_2d_3)   # [1 5 6 2 3 4]



# APPEND

arr1 = np.array([10,20,30])

new_arr1 =  np.append(arr1,[40,50,60])
print(new_arr1)    # => [10 20 30 40 50 60]
