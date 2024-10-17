from item import Item

item1 = Item("myItem", 750)
item1.name = "OtherItem" #Try to configure this to have more than ten characters. You will get an error.

item1.apply_icrement(0.2)
item1.apply_discount()

print(item1.name)
print(item1.price)

#Abstraction

item1 = Item("myItem", 750, 6)

item1.send_email()

#Inheritance
from phone import Phone
from keyboard1 import Keyboard

item1 = Phone("jscPhone", 1000, 3)
item2 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_icrement(0.2)
item2.apply_discount()

print(item1.price)
print(item2.price)
