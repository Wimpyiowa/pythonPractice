import numpy as np
#Remember to pip install numpy

#The Basics
a = np.array([1,2,3], dtype = "int16") #1D array, setting data type
print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]]) #2D array
print(b)

#Get Dimension
print(a.ndim)

#Get shape
print(b.shape) #2x3

#Get Type
print(a.dtype)

#Get Size
print(a.itemsize)
print(b.itemsize)

#Get Total Size
print(a.size * a.itemsize)
#or
print(a.nbytes)

#Accessing/Changing specific elements, rows, columns, etc
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)

#Get a specific element [r, c]
print(a[1,5])

#Get a specific row
print(a[0, :])

#Get a specific column
print(a[:, 2])

# Get a little more fancy [startindex:endindex:step]
print(a[0, 1:6:2])

# Change a value
a[1,5] = 20
print(a[1,5])

a[:, 2] = 5
print(a)

#3D Example
b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(b)

#Get a specific element (work outside in)
print(b[0, 1, 1]) #Grab the first outside shape, then select the row and index

# Replace
b[:,1,:] = [[9,9], [8,8]] #Changes all values on the second row (index 1)
print(b)