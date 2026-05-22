import numpy as np
arr=np.array([
            [['a','b','c'],['a','f','c']],
            [['a','b','c'],['a','b','c']],
            [['a','b','c'],['a','b','c']]
            ])
print(arr)
print(arr.ndim)
print(arr.shape) #-->gives out a tuple containing 3 values:depth of array,rows in each block,column in each row
print(arr[0][1][1]) # or arr[0,1,1]