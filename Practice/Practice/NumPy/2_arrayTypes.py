import numpy as np

a = np.array([[2,2], [2,2]])
print(a)

# All 0s matrix
print(np.zeros((2,3,4,6)))

#ones
print(np.ones((4,2,2), dtype="int32"))

#Any other number
print(np.full((2,2), 99)) #First clarify the shape, then the value.

#Any other number (full_like)
print(np.full_like(a, 4)) #grabs the shape of a, then fills the numbers with 4

#Random decimal numbers
print(np.random.rand(4,2,3))
print(np.random.random_sample(a.shape))

#Random Integer values
print(np.random.randint(7, size=(3,3))) #Size sets the shape.

#The identity matrix
print(np.identity(5))

#Repeat
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

#Test - Make number 1 go on the edges of a 5x5 grid, while having 9 in the middle. The rest of the numbers should be zero

chal = np.ones((5, 5))
print(chal)

chal2 = np.zeros((3,3))
print(chal2)

chal2[1,1] = 9
chal[1:4, 1:4] = chal2
print(chal)

#Be careful when copying arrays.

a = np.array([1,2,3])
b = a
b[0] = 4 #A will now print out this same replacement. Why? Shared memory. Do not copy like this.
#Do this instead.
b = a.copy()
b[0] = 100
print(b)
print(a)