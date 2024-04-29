import threading 
import socket 

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except Exception:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('utf-8'))
            nickname.remove(nickname)
            break 


def receive():
    while True:
        client,adress = server_socket.accept()
        print(f'connected with {adress} ')
        client.send("NICKNAME:".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        print(f'nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('utf-8'))
        client.send("connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle,args=(client))
        thread.start()
print("server is listening")
receive()





