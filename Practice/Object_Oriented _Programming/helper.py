#When to use class methods and when to use static methods ?

class Item:
    @staticmethod
    def is_integer(num):
        """
        This should do something that has a relationship 
        with the class, but not something that must be unique
        per instance.
        """

    @classmethod
    def instatiate_from_something(cls):
        """
        This should also do something that has a relationship
        with the class, but usually, those are used to
        manipulate different strcutures of data to instatiate
        objects like we have one with CSV
        """

#However, those could be also called from instances.

item1 = Item()
item1.is_integer(5)
item1.instatiate_from_something()