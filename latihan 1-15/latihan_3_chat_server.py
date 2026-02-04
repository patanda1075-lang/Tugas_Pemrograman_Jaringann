import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)

print("=== Terhubung ke Chat Server ===")

conn, addr = server.accept()

# Terima pesan pertama client
data = conn.recv(1024).decode('utf-8')
print(f'Client (Anda) -> "{data}"')

# Balasan server (TETAP, sesuai gambar)
reply = "Halo juga, nama aku Kesia"
print(f'Server  -> "{reply}"')
conn.send(reply.encode('utf-8'))

# Terima pesan kedua client
data2 = conn.recv(1024).decode('utf-8')
print(f'Client  -> "{data2}"')

conn.close()
server.close()
