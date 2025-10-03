import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
inserted_array = np.insert(array1, 2, [10, 11])  # Insert 10 and 11 at index 2
print(inserted_array)  # Output: [ 1  2 10 11  3  4  5]