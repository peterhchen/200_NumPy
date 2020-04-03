import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()  # copy does not share the reference data
y = arr.view()  # view share the reference data

print(x.base)
print(y.base)