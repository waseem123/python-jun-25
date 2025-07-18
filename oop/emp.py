class Employee:
    def __init__(self, name="<NAME>", per_day_salary=0, working_days=0):
        self.name = name
        self.per_day_salary = per_day_salary
        self.working_days = working_days

    def calculateMonthlySalary(self):
        self.monthly_salary = self.per_day_salary * self.working_days
        print("Monthly Salary: ", self.monthly_salary)

    def getEmployee(self):
        print("Name: ", self.name)
        print("Per day salary: ", self.per_day_salary)
        print("Working days: ", self.working_days)


e1 = Employee()
e1.getEmployee()
e1.calculateMonthlySalary()
print("_____________")

e2 = Employee("XYZ", 700, 26)
e2.getEmployee()
e2.calculateMonthlySalary()
