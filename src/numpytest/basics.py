import numpy as np

a = np.arange(1,7)
b = a.reshape(2,3)
print(b[1,1])
c = b[np.newaxis, :]
print(c)
print(c[0,1,1])
d = b[:, np.newaxis]
print(d)
print(d[1,0,1])
e = d[:, np.newaxis]
print(e[1,0,0,1])
print(e.ndim)
print(a.shape, b.shape, c.shape, d.shape, e.shape)
f = np.array([[2],[2]])
g = np.array([[[2],[1],[1]]])
print(g.shape)
h = np.array([[[[1]],[[2]],[[3]]]])
print(h.shape)
print(h[0][2][0][0])
i = np.array([[1],[1],[1]])
print(i.shape)
