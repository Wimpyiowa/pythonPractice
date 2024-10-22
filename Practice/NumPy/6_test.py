import numpy as np
#If you're looking at this, read only the goal of this file. 
#I advise finding answers first before looking at the code.

#With a 5x5 grid, there are numbers that count from 1 to 30.
#How do you grab only 11, 12, 16, and 17 all at one in an index?

#Question two. How would you index an array diagonally, starting from number two to 20?

#Question three. How would you find index values 4,5,24,25,29, and 30?

test = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], 
                 [16,17,18,19,20], [21,22,23,24,25], [26,27,28,29,30]])
print(test)

#Answer 1
print(test[2:4, 0:2])

#Answer 2
print(test[[0,1,2,3], [1,2,3,4]])

#Don't worry if you didn't get this one, as it wasn't covered.
#This is more on how you would approach a new problem with 
#Everything else that was learned.

#Answer 3
print(test[[0,0,4,4,5,5], [3,4,3,4,3,4]]) #rows, columns.
#Incase you're confused.
#Or, for simplicity
print(test[[0,4,5], 3:])



