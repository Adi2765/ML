import numpy as np
arr=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]])
# for row selection
print(arr[0])         #slicing--> arr[start:end:step]  arr[0] returns first block/row
print()
print(arr[0:3])
print()
print(arr[1:4])
print()
print(arr[0:4:2])
print()
print(arr[::-1]) #-->returns reversed rows
print()
#for column section ---> arr[:,column_no]
print(arr[:,1]) #----> returns second column of all rows
print()
print(arr[:,0:4:2]) #--->prints column 0 to 3 with 2 steps
print()
print(arr[:,::-1]) #reversed columns
print()
# for row and column selection both
print(arr[0:2,0:2]) #--->first two row and first two columns
