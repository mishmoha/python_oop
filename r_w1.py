# Class, Objects and Methods

class Item:
    def calculate_total_price(self, x, y): 
        return x * y


item1 = Item()
item1.name = "phone" # hard coded attributes / solved ny __init__
item1.price = 100 # hard coded attributes
item1.quantity = 5 # hard coded attributes
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "laptop" # hard coded attributes
item2.price = 1000 # hard coded attributes
item2.quantity = 3  # hard coded attributes
print(item2.calculate_total_price(item2.price, item2.quantity))
