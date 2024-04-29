import socket 
import threading 

nickname = input('choose nick name')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(socket.gethostname()),5050))
def recieve():
    while True:
        try:
            messange = client.recv(1024).decode('utf-8')
            if messange == "NICKNAME":
                client.send(nickname.encode('utf-8'))
            else:
                print(messange)
        except Exception:
            print('an error occured ')
            client.close()
            break
def write():
    while True:
        messange = f"{nickname}: {input('')}"
        client.send(messange.encode('utf-8'))


recieve_thread = threading.Thread(target=recieve).start()
write_thread = threading.Thread(target=write).start()

