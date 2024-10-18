#Dictionaries

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name = "Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

mydict["email"] = "max@xyz.com"
print(mydict)

del mydict["name"] #Deletes name from dictionary
print(mydict)

mydict.pop("age") #Another way to delete values from a dictionary. In this instance, it removes age.
print(mydict)

mydict.popitem() #Removes the last index in this dictionary. So this should remove email.
print(mydict)

if "city" in mydict:
    print(mydict["city"])

try:
    print(mydict["city"])  #If the value is not found, it will print out the exception, "Error."
except:
    print("Error")

for key in mydict: #Will loop through the dictionary values.
    print(key)

for key in mydict.keys(): #Will print in list form, only giving you the variable name
    print(key)

for value in mydict.values(): #Will print on different lines and the value.
    print(value)

for key, value in mydict.items(): #Prints on different lines, including both the variable name and value on the same line.
    print(key, value)

mydict_cpy = mydict #The copy and original will hold the same memory
mydict_cpy2 = mydict.copy() #Seperates their memory. You could also use mydict_cpy2 = dict(mydict)
print(mydict_cpy)

mydict_cpy2["email"] = "max@xyz.com"
print(mydict_cpy2)
print(mydict)

my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}

my_dict2 = dict(name = "Mary", age=27, city="Boston")

my_dict.update(my_dict2)
print(my_dict)

#Mutable
my_mutable = {3: 9, 6: 36, 9: 81}
print(my_mutable)

value = my_mutable[3]
print(value)

mytuple = (8,7) #A list is not possible here. []
mydict = {mytuple: 15} 

print(mydict)