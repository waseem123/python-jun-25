student = {
    'rollno':101,
    'name':'George',
    'marks':98
}

print(student)

student['school'] = 'XYZ School'
print(student)

student.update({'std':5,'div':'B'})
print(student)

student['div'] = 'A'
student['std'] = 7
print(student)

student.update({'rollno':202,'marks':88})
print(student)