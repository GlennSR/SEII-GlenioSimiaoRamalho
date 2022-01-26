import socket
import select

UDP_IP = "127.0.0.1"  # Endereço de IP do servidor
IN_PORT = 5005  # Porta
timeout = 3  # Tempo de timeout


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializa o socket
sock.bind((UDP_IP, IN_PORT))  # Associa o socket com o endereço local, esse é o servidor

while True:
    data, addr = sock.recvfrom(1024)  # Recebe os primeiros dados do remetente
    if data:
        print("File name:", data)
        file_name = data.strip()  # Remove espaços desnecessários

    f = open(file_name + '2', 'wb')  # Abre um arquivo como escrita

    while True:
        ready = select.select([sock], [], [], timeout)  # fornece a multiplexação de E/S fornecida pela chamada de
        # função Unix select().
        # select() é uma chamada de sistema. Ele diz ao kernel para notificar quando qualquer um dos descritores nos
        # conjuntos estiver pronto para condições de leitura/gravação/exceção.
        if ready[0]:
            data, addr = sock.recvfrom(1024)  # Recebe os dados do socket
            f.write(data)  # Escreve esses dados no novo arquivo
        else:
            print("%s Finish!" % file_name)
            f.close()  # Fecha o arquivo
            break
