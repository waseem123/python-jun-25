class box:
    def set_box(self, width=0, height=0):
        self.width = width
        self.height = height

    def get_box(self):
        print(f'Width:{self.width}, Height:{self.height}')


class colored_box(box):
    def set_colored_box(self, color):
        self.color = color

    def get_colored_box(self):
        print(f'Color:{self.color}')


class shipped_box(colored_box):
    def set_shipped_box(self, weight=0, shipping_cost=0):
        self.weight = weight
        self.shipping_cost = shipping_cost

    def get_shipped_box(self):
        print(f'Weight:{self.weight}, Shipping Cost:{self.shipping_cost}')

s = shipped_box()
s.set_box(100,50)
s.set_colored_box("Brown")
s.set_shipped_box(5,100)

s.get_box()
s.get_colored_box()
s.get_shipped_box()