import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.1.8.70"

ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


def receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                print("Desconectado pelo servidor")
                break
            print(msg + '\n')
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            break


def send(msg):
    try:
        client.send(msg.encode(FORMAT))
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")


thread1 = threading.Thread(target=receive)
thread1.start()

while True:
    msg = input()
    if msg == DISCONNECT_MESSAGE:
        send(msg)
        break
    send(msg)

thread1.join()
client.close()
