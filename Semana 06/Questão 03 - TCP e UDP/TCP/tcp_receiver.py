import socket

TCP_IP = "127.0.0.1"  # Define o endereço de IP do sevidor
FILE_PORT = 5005  # Define a porta para o arquivo
DATA_PORT = 5006  # Define a porta para os dados
timeout = 3  # Tempo de timeout
buf = 1024  # Tamanho do buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Inicializa o socket
sock_f.bind((TCP_IP, FILE_PORT))  # Associa o socket com o endereço local, esse é o servidor
sock_f.listen(1)  # Começa a "ouvir" pôr clientes que queiram se conectar

# Mesma coisa de cima, mas agora para os dados
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT))
sock_d.listen(1)


while True:
    conn, addr = sock_f.accept()  # Aceita conexão do cliente
    data = conn.recv(buf)  # Recebe o nome do arquivo
    if data:
        print("File name:", data)
        file_name = data.strip()  # Remove espaços desnecessários

    f = open(file_name, 'wb')  # Abre o arquivo

    conn, addr = sock_d.accept()  # Aceita conexão do cliente
    while True:
        data = conn.recv(buf)  # Recebe os dados
        if not data:  # Se nulo, pára
            break
        f.write(data)  # Escreve os dados no arquivo

    print("%s Finish!" % file_name)
    f.close()  # Fecha a conexão
