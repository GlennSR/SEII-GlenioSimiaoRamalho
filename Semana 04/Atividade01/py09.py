import sys

import my_module as mm

courses = ['Historia', 'Matematica', 'Fisica', 'Arte']

index = mm.find_index(courses, 'Matematica')
print(index)

print(sys.path)


import random

courses = ['Historia', 'Matematica', 'Fisica', 'Arte']

random_course = random.choice(courses)
print(random_course)
