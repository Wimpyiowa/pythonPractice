import numpy as np

fileData = np.genfromtxt('data.txt', delimiter=',')
fileData = fileData.astype('int32')
print(fileData)

#Boolean Masking and Advanced Indexing
print(fileData > 50)
print(fileData[fileData > 50]) #Grabs the index that has numbers higher than 50
print(np.any(fileData > 50, axis=0))
print(((fileData > 50) & (fileData < 100)))
print(~(((fileData > 50) & (fileData < 100)))) #Not greater than 50

#You can index with a list in NumPy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

