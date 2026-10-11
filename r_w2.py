# constructor, __init__, (you can also add other attributes to instances apart from the ones added in the constructor, in case where e.g you dont know the quantity you can set it tom0mat the method and not place it in the instance)
# run validations, instance attributes

class Item:
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


item1 = Item("phone", 100, 5)

print(item1.calculate_total_price())


item2 = Item("laptop", 1000,  3)
 
print(item2.calculate_total_price())
