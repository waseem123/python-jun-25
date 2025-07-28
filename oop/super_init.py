class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def getData(self):
        print(f'TITLE - {self.title}')
        print(f'AUTHOR - {self.author}')


class ProgrammingBook(Book):
    def __init__(self, title, author, noOfPages, price):
        super().__init__(title, author)
        self.noOfPages = noOfPages
        self.price = price

    def getData(self):
        super().getData()
        print(f'NO OF PAGES - {self.noOfPages}')
        print(f'PRICE - {self.price}')


p = ProgrammingBook("Programming In C", "Denise Richie", 100, 1000)
p.getData()
