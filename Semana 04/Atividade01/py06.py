
language = 'Python'

if language == 'Python':
    print('A linguagem é Python')
elif language == 'Java':
    print('A linguagem é Java')
else:
    print('Não é Python')


user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Incorrect creds')


a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(a is b)
