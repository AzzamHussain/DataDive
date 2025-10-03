import numpy as np
array1=np.array([1,2,3,4,5,6,7,8,9])
print(array1[2:8:2])  # it will print from index 2 to index 7 with a step of 2
print(array1[:6])  # it will print from start to index 5
print(array1[4:])  # it will print from index 4 to the end
print(array1[::4])  # it will print from index 0 to the end with a step of 2