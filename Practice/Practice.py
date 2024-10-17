#List

mylist = ["banana", "cherry", "apple"]
print(mylist)

for i in mylist:
    print(i)

if "apple" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist)) #Checks the length of the list.

mylist.append("lemon")  #Add to the list
print(mylist)

mylist.insert(1, "blueberry") #Adding to a list at a specific index
print(mylist)

item = mylist.pop() #Removes the last index
print(item)
print(mylist)

item = mylist.remove("cherry") #Remove a specific value by calling its value.
print(item) 

item = mylist.clear() #Clears all values, making the list empty.

item = mylist.reverse() #Reverses the values. ex. last value becomes first value.

myNumbers = [4, 1, 5, -8, 10]
print(myNumbers)

item2 = myNumbers.sort()
print(myNumbers)   #Sorts all the numbers.. Confused why you can't call item2 though.

new_numbers = sorted(myNumbers)
print(new_numbers) #Previous method has the function already created within lists. To sort this on a differnt variable, use this method.


Numbers2 = [0] * 5 #Easier way to put multiple values of the same.
print(Numbers2)

Numbers3 = [1,1,1,1,1]
 
new_numbers = Numbers2 + Numbers3  #Self explainitory.
print(new_numbers)

newList = [1,2,3,4,4,4,5]

a = newList[1:5] #Slicing. If you remove the first value, this will read every value from 0 to the end. And vice versa.
print(a)

b = newList[::2] #Steps. You can add how much "steps" this will read. So, this should print [1, 3, 4..] You can also start at a specific point using the starting value.
c = newList[::-1] #Reversed.

listOrg = ["banana", "cheery", "apple"]

listCpy = listOrg 

listCpy.append("lemon") #This will change both lists as they serve the same memory.

print(listCpy)

listCpy2 = listOrg.copy() #This will fix the previous method. Could use do listCpy2 = list(listOrg)

listCpy2.append("apple")

print (listCpy2)

comp1 = [1,2,2,3,4,4]
comp2 = [i*i for i in comp1] #Makes every value squared.

print(comp1)
print(comp2)