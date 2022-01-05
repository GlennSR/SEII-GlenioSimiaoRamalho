# DictWriter

from csv import DictWriter
from pathlib import Path

with open('filmes.csv', 'a', encoding='UTF-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)

    # Verificando se o arquivo já existe
    file_name = r'C:/Users/gleni/PycharmProjects/Curso_Python_Udemy/Manipulando Arquivos CSV e JSON/filmes.csv'
    file_obj = Path(file_name)
    if not file_obj.is_file():
        escritor_csv.writeheader() # Escreve o cabeçalho no arquivo
    filme = None
    while filme != 'sair':
        filme = input('Informe o título do filme: ')
        if filme.lower() != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})






# Reader

from csv import reader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pula o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} cm')
print()

# DictReader

from csv import DictReader

with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} cm")
print()

# DictReader com outro delimitador (Vale para reader também)

from csv import DictReader

with open('lutadores2.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=';')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} cm")