import os

print(os.getcwd())

os.chdir('/')

print(os.getcwd())
print(os.listdir())

# os.removedirs('py10Test')
# os.mkdir('py10Test')

# print(os.listdir())

# os.rename('py10Test', 'py10teste')
# print(os.listdir())

print(os.path.exists('tmp/fgfgfg'))
print(os.path.splitext('/tmp/test.txt'))
