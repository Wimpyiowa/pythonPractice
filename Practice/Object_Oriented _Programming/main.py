class Item:
    def calculate_total_price(self, x, y): #method
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

#constructor
class Item2:
    def __init__(self, name, price, quantity):
        print(f'An instance created: {name}')
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): #method
        return self.price * self.quantity
    
item1 = Item2("Phone", 100, 5)


item2 = Item2("Laptop", 1000, 3)

item2.has_numpad = False
print(item1.calculate_total_price())

#Design, expections.
class Operation:
    def __init__(self, name: str, price: float, quantity: int):
        print(f'An instance created: {name}')
        #Run validations to the recieved arguements
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): #method
        return self.price * self.quantity
    
item1 = Operation("Phone", 100, 5)


item2 = Operation("Laptop", 1000, 3)

item2.has_numpad = False
print(item1.calculate_total_price())

#Example two, class attributes
class Pay:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        print(f'An instance created: {name}')
        #Run validations to the recieved arguements
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Pay.all.append(self)

    def calculate_total_price(self): #method
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})" 
    
item1 = Pay("Phone", 100, 5)
item1.apply_discount()
print(item1.price)


item2 = Pay("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

item2.has_numpad = False

#print(Pay.__dict__) #All the attributes for Class level
#print(item1.__dict__) #All the attributes for Instance level

item3 = Pay("Cable", 10, 5)
item4 = Pay("Mouse", 50, 5)
item = Pay("Keyboard", 75, 5)

print(Pay.all)

for instance in Pay.all:
    print(instance.name)


#Class vs Static Methods, CSV (Comma Separated Values)
import csv

class CSV:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        print(f'An instance created: {name}')
        #Run validations to the recieved arguements
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        CSV.all.append(self)

    def calculate_total_price(self): #method
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            CSV(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are  point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})" 
    

CSV.instantiate_from_csv()
print(CSV.all)

print(CSV.is_integer(5))


#Inheritance

class Phone(CSV):
    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        print(f'An instance created: {name}')
        # Call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )

        #Run validations to the recieved arguements
        assert broken_phones >= 0, f"Price {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)

print(CSV.all)
print(Phone.all)
