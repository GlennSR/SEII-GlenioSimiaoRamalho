
student = {'name': 'Glenio', 'age': 25, 'courses': ['SSA', 'CVRM']}

print(student['courses'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))

student['phone'] = '555-555'
student['name'] = 'Lisa'

print(student)

student = {'name': 'Glenio', 'age': 25, 'courses': ['SSA', 'CVRM']}
student.update({'name': 'Lisa', 'age': 26, 'phone': '555-555'})
print(student)

del student['age']
print(student)

student = {'name': 'Glenio', 'age': 25, 'courses': ['SSA', 'CVRM']}
age = student.pop('age')
print(student)
print(age)

print(student.items())

student = {'name': 'Glenio', 'age': 25, 'courses': ['SSA', 'CVRM']}

for keys, values in student.items():
    print(keys, values)
