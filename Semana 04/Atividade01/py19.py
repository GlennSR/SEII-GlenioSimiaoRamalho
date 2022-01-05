# LISTA
lista = [9, 6, 1, 2, 6, 7, 2, 3, 8]

s_lista = sorted(lista)
print('Lista ordenada:\t', s_lista)

lista.sort()
print('Lista original:\t', lista)

lis2 = [-6, -5, -4, 1, 2, 3]
s_lis2 = sorted(lis2, key=abs)
print('Lista num ordenada pelo valor abs:\t', s_lis2)

# TUPLA
tupla = (9, 6, 1, 2, 6, 7, 2, 3, 8)
s_tupla = sorted(tupla)
print('Tupla ordenada:\t', s_tupla)

# DICIONARIO
dic = {'nome': 'Glênio', 'Emprego': 'Eng. Mecatronico', 'idade': None}
s_dic = sorted(dic)
print('Dicionario ordenado:\t', s_dic)

