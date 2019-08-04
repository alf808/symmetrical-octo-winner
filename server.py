#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(1)

while True:
    print('waiting for connection')
    conn, client_addr = sock.accept()
    # from_client = b''

    try:
        print(f'connection from {client_addr}')
        while True:
            data = conn.recv(4096)
            print(f'received {data}')
            if data:
                print('hello client. you are receiving data from server')
                # from_client += data
                # print(from_client)
                conn.send(data)
    finally:
        conn.close()
        print('client left')
