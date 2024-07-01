import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #local ip address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket
server.bind(ADDR) #binding the socket to the particular ip adress and port

def handle_client(conn, addr):
    print(f"new connection {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{addr} {msg}")
    conn.close()

def start():
    server.listen()
    print(f"the server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #when a new connection occurs we store the address of the connection in addr, conn contains an actual object that allows us to send a message back to the connection
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"active connections: {threading.active_count() - 1}")

print("SERVER is starting")
start()
