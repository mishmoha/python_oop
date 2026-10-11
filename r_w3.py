#class attributes
# instance level attributes and class level attributes

class Item:
    pay_rate = 0.8 # the pay rate after 20% discount || class atribute
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign tp self object
        self.name = name 
        self.price = price
        self.quantity = quantity
          

    def calculate_total_price(self): 
        return self.price * self.quantity

    def apply_discount (self):
        self.price = self.price * self.pay_rate


item1 = Item("phone", 100, 5)
item1.apply_discount()
print (item1.price)

item2 = Item("laptop", 1000,  3)
item2.pay_rate = 0.7
item2.apply_discount ()
print (item2.price)
#print(item1.calculate_total_price())

#print (Item.__dict__)# all attributes at class level
#print(item1.__dict__) # all  attributes at intsnace level


 
#print(item2.calculate_total_price())
