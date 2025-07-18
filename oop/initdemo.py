class Bottle:
    def __init__(t, material="NA", quantity=0, price=0.0):
        print("init executed")
        t.material = material
        t.quantity = quantity
        t.price = price

    def get_bottle(self):
        print(f'Material: {self.material}')
        print(f'Quantity: {self.quantity}')
        print(f'Price   : {self.price}')

b1 = Bottle("Plastic", 1, 20)
b1.get_bottle()
print("________________")
b2 = Bottle("Steel", 1, 200)
b2.get_bottle()
print("________________")
b3 = Bottle()
b3.get_bottle()
print("________________")
b4 = Bottle(quantity=2, material="Plastic", price=32.25)
b4.get_bottle()
print("________________")