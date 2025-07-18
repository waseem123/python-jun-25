class Student:
    rollno = 0
    name = ""
    marks = 0

    def setStudent(self):
        self.rollno = int(input("Enter roll no: "))
        self.name = input("Enter name: ")
        self.marks = int(input("Enter marks out of 300: "))

    def getStudent(self):
        print("ROLL NO : ", self.rollno)
        print("NAME : ", self.name)
        print("MARKS : ", self.marks)

    def calculate_percentage(self):
        self.percentage = ((self.marks * 100) / 300)
        print("PERCENTAGE : ", self.percentage)


s1 = Student()
s2 = Student()

s1.setStudent()
s2.setStudent()
print("_________________")
s1.getStudent()
s1.calculate_percentage()
print('---------------')
s2.getStudent()
