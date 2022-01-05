'''
LEGB
Local, Enclosing, Global, Built-in
'''

for a in range(2):
    x = f'global {a}'


def outer():
    # x = 'outer x'
    for b in range(3):
        x = f'outer {b}'

    def inner():
        # x = 'inner x'
        for c in range(4):
            x = f'inner {c}'
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)

outer()
print(x)
print(a)