f = open('test.txt', 'r')
print(f.name)
print(f.mode)
f.close()

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    pass

with open('test.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents, end='')
    pass

print(f.closed)

with open('test2.txt', 'w') as f:
    f.write('Test')
