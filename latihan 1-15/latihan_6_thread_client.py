import socket
import threading
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg:
                print(msg, end="")
        except:
            break

# thread penerima pesan
threading.Thread(target=receive, daemon=True).start()

messages = [
    '"halo gays"',
    '"selamat datang di fikom"',
    '"universitas indonesia timur"'
]

for msg in messages:
    client.send(msg.encode('utf-8'))
    time.sleep(1)

time.sleep(2)
client.close()
