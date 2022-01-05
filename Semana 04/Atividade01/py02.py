
message = 'Glênio\'s World'

print(message)
print(len(message))
print(message[0:8])
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))
print(message.replace('World', 'Universe'))

##################

greeting = 'Hello'
name = 'Bob'

msg = greeting + ', ' + name
print(msg)

msg2 = f'{greeting}, {name}'
print(msg2)

print(dir(name))
print(help(str.lower))
