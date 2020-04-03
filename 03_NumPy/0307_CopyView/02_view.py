import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# View creates two reference but share the data 
x = arr.view()
arr[0] = 42

print(arr)
print(x)