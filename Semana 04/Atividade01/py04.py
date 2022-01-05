
cursos = ['Historia', 'Matematica', 'Fisica', 'Computacao']

cursos.append('Arte')
cursos.insert(0, 'Biologia')
print(cursos)

cursos2 = ['Educacao Fisica', 'Calculo']

cursos.insert(0, cursos2)
print(cursos)

cursos.extend(cursos2)
print(cursos)

cursos.remove('Matematica')
print(cursos)

popped = cursos.pop()
print(popped)

cursos = ['Historia', 'Matematica', 'Fisica', 'Computacao']

cursos.reverse()
print(cursos)

cursos.sort()
print(cursos)

nums = [5, 6, 7, 2, 3, 1]

nums.sort(reverse=True)
print(nums)

sorted_nums = sorted(nums)
print(sorted_nums)

print(sum(nums))

print(cursos.index('Matematica'))

cursos = ['Historia', 'Matematica', 'Fisica', 'Computacao']

cursos_str = ' - '.join(cursos)
print(cursos_str)

nova_lista = cursos_str.split(' - ')
print(nova_lista)


##############################"

# Mutavel
lista_1 = ['Historia', 'Matematica', 'Fisica', 'Computacao']
lista_2 = lista_1

print(lista_1)
print(lista_2)

lista_1[0] = 'Art'

print(lista_1)
print(lista_2)


# Imutavel
tupla_1 = ('Historia', 'Matematica', 'Fisica', 'Computacao')
tupla_2 = tupla_1

print(tupla_1)
print(tupla_2)

# tupla_1[0] = 'Art'

print(tupla_1)
print(tupla_2)

# Sets
cs_courses = {'Historia', 'Matematica', 'Fisica', 'Computacao'}

print(cs_courses)

