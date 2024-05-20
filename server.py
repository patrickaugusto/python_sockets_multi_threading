import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []


def broadcast(msg, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(msg.encode(FORMAT))
            except:
                client.close()
                remove(client)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    clients.append(conn)
    while connected:
        try:
            msg = conn.recv(2048).decode(FORMAT)
            if not msg:
                break
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DISCONNECTED] {addr} disconnected.")
                broadcast(f"[DISCONNECTED] {addr} disconnected.", conn)
            else:
                print(f"[{addr}] {msg}")
                broadcast(f"[{addr}] {msg}", conn)
        except Exception as e:
            print(f"Error handling client: {e}")
            break
    conn.close()
    remove(conn)


def remove(conn):
    if conn in clients:
        clients.remove(conn)


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
