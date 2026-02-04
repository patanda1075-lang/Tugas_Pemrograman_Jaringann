import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

# Pesan client (dibuat statis)
msg1 = "Halo, kalau boleh tau nama kamu siapa?"
msg2 = "Senang berkenalan dengan anda"

# Kirim pesan pertama
print(f'Client  -> "{msg1}"')
client.send(msg1.encode('utf-8'))

# Terima balasan server
reply = client.recv(1024).decode('utf-8')
print(f'Server anda  -> "{reply}"')

# Kirim pesan kedua
print(f'Client  -> "{msg2}"')
client.send(msg2.encode('utf-8'))

client.close()
