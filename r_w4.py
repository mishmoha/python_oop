# using the clas attribute "all" to access all of our instances
# append
# __repr__ used to represent objects in an unserstandable format

class Item:
    pay_rate = 0.8 # the pay rate after 20% discount || class atribute
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name 
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append (self)         

    def calculate_total_price(self): 
        return self.price * self.quantity

    def apply_discount (self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("phone", 100, 1)
item2 = Item("laptop", 1000, 3)
item3 = Item("cable", 10, 5)
item4 = Item("mouse", 50, 5)
item5 = Item("keyboard", 75, 5)

print(Item.all)  