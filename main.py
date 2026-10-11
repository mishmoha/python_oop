# main program used to instantiate instances only
from item import Item
from phone import Phone

item1 = Item("MyItem", 750, 6)
item1 = Phone("Mish", 1000, 50)
item1.send_email()



