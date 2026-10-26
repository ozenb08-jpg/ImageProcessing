import numpy as np

a = np.array([
    [10, 100, 200],
    [50, 150, 250]
], dtype=np.uint8)

print("dtype:", a.dtype)
print("shape:", a.shape)
print("ndim:", a.ndim)
print("size:", a.size)
print("nbytes:", a.nbytes)
print("a[1, 2]:", a[1, 2])
print("a[0, 1]:", a[0, 1])
print("a + 10:", a + 10)
print("a - 20:", a - 20)
print("a * 2:", a * 2)
print("max:", a.max())
print("max axis 0:", a.max(axis=0))
print("max axis 1:", a.max(axis=1))