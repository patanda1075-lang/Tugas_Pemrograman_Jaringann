import asyncio

async def main():
    # Menghubungkan client ke server
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888
    )

    addr = writer.get_extra_info('peername')
    print(f"=== Terhubung ke server sebagai {addr} ===")

    # -----------------------------------------
    # 3 teks yang dikirim ke server
    # -----------------------------------------
    pesan = [
        "selamat siang",
        "kamu lagi apa",
        "kamu lagi di mana"
    ]

    for teks in pesan:
        print("Client >", teks)

        # Kirim pesan ke server
        writer.write((teks + "\n").encode())
        await writer.drain()

        # Terima balasan dari server
        data = await reader.read(100)
        print("Server >", data.decode().strip())

    # Tutup koneksi
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
