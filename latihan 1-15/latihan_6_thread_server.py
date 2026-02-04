import socket
import threading

clients = []
lock = threading.Lock()

def broadcast(message):
    with lock:
        for client in clients:
            try:
                client.send(message)
            except:
                client.close()

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    with lock:
        clients.append(conn)

    # 🔥 welcome dikirim ke client
    conn.send("Selamat datang di Chat Room!\n".encode('utf-8'))

    try:
        while True:
            message = conn.recv(1024)
            if not message:
                break

            msg = message.decode('utf-8')
            print(f"[{addr[1]}]: {msg}")

            # kirim apa adanya ke client lain
            broadcast((msg + "\n").encode('utf-8'))

    except:
        pass
    finally:
        print(f"[DISCONNECT] {addr} keluar.")
        with lock:
            clients.remove(conn)
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen()
    print("[SERVER STARTED] Menunggu di port 5555...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
