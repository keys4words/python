import numpy as np

nlist = [1, 2, 3, 4, 5, 6]

nparray = np.array(nlist)
print(nparray, type(nparray))

a = np.array([1, 2, 3])
b = np.array([[1,2], [3, 4], [5, 6]])
print(a[0])
print(b[1][0])
M = np.matrix([[1,2], [3, 4], [5, 6]])
print(M)
print(b[1, 0])
# print(b.T)
print(b.shape)
c = b.T
print(c.shape)
print(b.ndim, b.size, b.dtype)
d = np.array([1.1, 1.3])
print(d.dtype)
e = np.array([1, 3], dtype=np.float64)
print(e)
print(b, b.itemsize)
print(e, e.itemsize)
print(a, a.min())
print(a.max())
print(a.sum())
print(b, b.sum(axis=1))
