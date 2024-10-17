import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):

       
        print(f'An instance created: {name}')
        #Run validations to the recieved arguements
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.__name = name #Use an underscore or two if we are using @property. This will become a private attribute.
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self): #We cut this function to place it inside our property.
        self.__price = self.__price * self.pay_rate

    def apply_icrement(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter  #Allows users to set the name now in main2Example.py
    def name(self, value):
        if len(value) > 10: #Encapsulation.
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self): #method
        return self.__price * self.quantity
    


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
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


    #Not actually sending an email. This is an example of what is needed on the back-end. So, we'll use pass to execute this code without raising errors (leaving a line empty)
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.__price}, {self.quantity})" 
    
    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        pass

    def __prepare_body(self):
        return f"""
        Hello someone
        We have {self.name} {self.quantity} times.
        Regards, mother
        """
    
    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()