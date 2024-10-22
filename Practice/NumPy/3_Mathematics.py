import numpy as np

a = np.array([1,2,3,4])
a = a + 2
print(a)

a = a * 2
print(a)

b = np.array([1,0,1,0])
print (a + b)

#Take the sin
print(np.sin(a))

#Linear Algrebra
a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

print(np.matmul(a,b))

# Find the determinant
c = np.identity(3)
print(np.linalg.det(c))

#Statistics
stats = np.array([[1,2,3], [4,5,6]])
print(stats)

print(np.min(stats, axis=1))

print(np.max(stats, axis=1))

print(np.sum(stats, axis=0))