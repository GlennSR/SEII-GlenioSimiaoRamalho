import socket
import threading
import time

PORT = 5050
FORMATO = 'utf-8'
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def handle_mensagens():
    while True:
        msg = client.recv(1024).decode()
        mensagem_separada = msg.split("=")
        print(mensagem_separada[1] + ": " + mensagem_separada[2])


def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))


def enviar_mensagem():
    mensagem = input()
    enviar("msg=" + mensagem)


def enviar_nome():
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)


def iniciar_envio():
    enviar_nome()
    enviar_mensagem()


def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    iniciar()
