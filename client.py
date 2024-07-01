import socket 

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #local ip address
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message) 
    send_length = str(msg_length).encode(FORMAT) #sending the length of the message
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("yooo wassgood")
