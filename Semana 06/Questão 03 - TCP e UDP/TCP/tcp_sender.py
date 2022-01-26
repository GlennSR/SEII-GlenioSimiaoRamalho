import socket
import sys

TCP_IP = "127.0.0.1"  # Endereço de IP do servidor
FILE_PORT = 5005  # Define a porta para o arquivo
DATA_PORT = 5006  # Define a porta para os dados
buf = 1024  # Tamanho do buffer
file_name = sys.argv[1]  # O Nome do arquivo será passado como entrada pelo terminal


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Inicializa o socket
    sock.connect((TCP_IP, FILE_PORT))  # Estabelece a conexão com o host remoto
    sock.send(file_name)  # envia o nome do arquivo
    sock.close()  # Fecha o socket

    print("Sending %s ..." % file_name)

    f = open(file_name, "rb")  # Abre o arquivo de mídia
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Inicia um segundo socket
    sock.connect((TCP_IP, DATA_PORT))  # Estabelece a conexão com a porta dos dados
    data = f.read()  # Lê os dados do arquivo
    sock.send(data)  # Envia os dados

finally:
    sock.close()  # Fecha a conexão
    f.close()  # Fecha o arquivo
