import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer, programmer"]}

personJSON = json.dumps(person) #Now encodes in JSON format
print(personJSON)

personJSON = json.dumps(person, indent=4) #Looks nicer, wowie!
print(personJSON)

personJSON = json.dumps(person, indent=4, separators=('; ', '= ')) #If you have eyes, you will understand this change. Isn't recommended to do this anyway.
print(personJSON)

personJSON = json.dumps(person, indent=4, sort_keys=True) #Sorts in ABC format. Go back to kindergarden!
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


#Decoding
person = json.loads(personJSON)
print(person)

#OR

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)


#Woo class time

class User:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
user = User('Max', 27)

def encode_user(o): #Have to create this function in order to encode a python object
    if isinstance (o, User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Object of type Yser is not JSON serialiable')


from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance (o, User):
            return{'name': o.name, 'age': o.age, o.__class__.__name__:True} 
        return JSONEncoder.default(self, o)
    
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

#OR

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)

#More decoding..

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)