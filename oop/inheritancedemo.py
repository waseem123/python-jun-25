class person:
    def set_person(self, name="", city="", blood_group=""):
        self.name = name
        self.city = city
        self.blood_group = blood_group

    def get_person(self):
        print(f'Name - {self.name}')
        print(f'City - {self.city}')
        print(f'Blood group - {self.blood_group}')


class student(person):
    def set_student(self, roll_no=0, std="", div=""):
        self.roll_no = roll_no
        self.std = std
        self.div = div

    def get_student(self):
        print(f'roll no - {self.roll_no}')
        print(f'std - {self.std}')
        print(f'div - {self.div}')


# p = person()
# p.set_person(name="Alex", city="LA", blood_group="B+")
# p.get_person()

print("_____________________")

s = student()
s.set_person(name="Alex", city="LA", blood_group="B+")
s.set_student(roll_no=123, std="Vth", div="A")
s.get_person()
s.get_student()
