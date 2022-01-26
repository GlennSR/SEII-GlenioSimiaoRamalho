import socket
import time
import sys

UDP_IP = "127.0.0.1"  # Endereço de IP do servidor
UDP_PORT = 5005  # Porta
buf = 1024  # Tamanho do buffer
file_name = sys.argv[1]  # O Nome do arquivo será passado como entrada pelo terminal


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializa o socket
sock.sendto(file_name, (UDP_IP, UDP_PORT))  # Envia o nome do arquivo para o endereço IP e a porta definidos
print("Sending %s ..." % file_name)

f = open(file_name, "r")  # Abre o arquivo para leitura
data = f.read(buf)  # Lê os dados com o tamanho escolhido
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):  # Envia os dados para o endereço IP e porta definidos
        data = f.read(buf)  # Lê mais um pouco do arquivo, até ler tudo
        time.sleep(0.02) # Dando tempo ao destinatário para salvar os dados recebidos

sock.close()  # Fecha a conexão
f.close()  # Fecha o arquivo
