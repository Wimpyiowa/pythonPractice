import numpy as np

fileData = np.genfromtxt('data.txt', delimiter=',')
fileData.astype('int32')
print(fileData)