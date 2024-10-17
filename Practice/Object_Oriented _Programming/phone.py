from item import Item

class Phone(Item):
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