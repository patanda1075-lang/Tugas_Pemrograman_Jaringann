import socket
import select
import sys

def run_chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9000))

    print("=== Terhubung ke Chat Server ===")
    print("Ketik pesan dan tekan ENTER (CTRL+C untuk keluar)")

    while True:
        # ---------------------------------------------
        # KESALAHAN SENGAJA:
        # sys.stdin BUKAN socket di Windows
        # ---------------------------------------------
        sockets_list = [sys.stdin, client_socket]

        read_sockets, _, _ = select.select(sockets_list, [], [])

        for sock in read_sockets:
            if sock == client_socket:
                data = sock.recv(1024)
                if not data:
                    print("[KELUAR] Server menutup koneksi")
                    sys.exit()
                else:
                    print(data.decode())

            else:
                # Input dari keyboard
                msg = sys.stdin.readline()
                client_socket.send(msg.encode())

if __name__ == "__main__":
    run_chat_client()
