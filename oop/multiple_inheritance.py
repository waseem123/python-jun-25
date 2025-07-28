class Watch:
    def setWatch(self, brand, type):
        self.brand = brand
        self.type = type
        self.features = ['Date', 'Time', 'Timer', 'Alarm', 'Stopwatch']

    def getWatch(self):
        print(f'Brand - {self.brand}')
        print(f'Type - {self.type}')

    def getFeatures(self):
        print(f'Features - {self.features}')


class Android:
    def getSmartFeatures(self):
        self.smartFeatures = ['Notifications', 'Calling and SMS', 'Fitness Tracker', 'Music Player']
        print(f'Smart Features - {self.smartFeatures}')


class SmartWatch(Watch, Android):
    def setSmartWatch(self, color, price, shape):
        self.color = color
        self.price = price
        self.shape = shape

    def getSmartWatch(self):
        print(f'Color - {self.color}')
        print(f'Price - {self.price}')
        print(f'Shape - {self.shape}')


sm = SmartWatch()
sm.setWatch('boAt', 'Digital')
sm.setSmartWatch('Black', 'INR. 6500', 'Circle')

sm.getWatch()
sm.getSmartWatch()
sm.getFeatures()
sm.getSmartFeatures()
