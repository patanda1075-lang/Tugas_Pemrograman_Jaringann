import asyncio

async def handle_client(reader, writer):
    """
    Coroutine ini akan dijalankan untuk SETIAP client yang connect.
    Bayangkan ini sebagai 'Langkah Catur' untuk satu meja.
    """
    addr = writer.get_extra_info('peername')
    print(f"[BARU] Koneksi dari {addr}")

    try:
        while True:
            # 1. Baca Data (Non-Blocking)
            # await artinya menunggu data TANPA memblokir server
            data = await reader.read(100)

            # Jika client menutup koneksi
            if not data:
                print(f"[PUTUS] {addr} menutup koneksi.")
                break

            message = data.decode().strip()
            print(f"[{addr}] Mengirim: {message}")

            # 2. Proses & Balas (Echo)
            response = f"Echo: {message}\n"
            writer.write(response.encode())

            # 3. Pastikan data terkirim
            await writer.drain()

    except Exception as e:
        print(f"[ERROR] {addr}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    # Membuat Server Async
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888
    )

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"=== Async Server Berjalan di {addrs} ===")

    # Server berjalan terus
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer Dimatikan.")
