class Bag:
    def setData(self, brand, color):
        self.brand = brand
        self.color = color

    def getData(self):
        print(self.brand, self.color)


class LaptopBag(Bag):
    def setData(self, brand, color, material, price):
        super().setData(brand, color)
        self.material = material
        self.price = price

    def getData(self):
        super().getData()
        print(self.material, self.price)


l = LaptopBag()
l.setData('American Tourister', 'Glossy Brown', 'Leather', '4500')
l.getData()
