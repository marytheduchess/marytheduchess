import numpy as np

a = np.array([1, 2, 3])
print(a.size)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b.nbytes)



# Get dimension of arrays (print)
a.ndim
# Get shape
a.shape
b.shape
# Get type 
a.dtype
# Get size
a.itemsize
# Get total size
a.size * a.itemsize
#also equals
a.nbytes 

# How to access/change specific elements, rows columns etc.
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
#Get a spec. element [row, column]
a[1, 5]



