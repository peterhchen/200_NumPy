import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)
# -1 is unknown dimension. SO only [2, 2]

print(newarr)