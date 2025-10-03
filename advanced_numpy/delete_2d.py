import numpy as np
array_2d=np.array([[6,7,8,9,10],[11,12,13,14,15]])
print(array_2d)
deleted_array=np.delete(array_2d,0,axis=0) # it will delete 1st row
print(deleted_array)