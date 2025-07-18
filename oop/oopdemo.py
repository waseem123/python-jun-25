x = 10.0

class Person:
    aadhar_no = 123456789012
    name = "John"
    city = "San Francisco"

p1 = Person()
p2 = Person()

print(p1.aadhar_no, p1.city, p1.name)

p2.city = "Los Angeles"
p2.name = "Roger"
p2.aadhar_no = 987654321
print(p2.aadhar_no, p2.city, p2.name)

p3 = Person()
p4 = Person()
print(p3.aadhar_no, p3.city, p3.name)
print(p4.city, p4.name)