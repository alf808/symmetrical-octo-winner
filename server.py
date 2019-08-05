#!/usr/bin/python3
import socket
import sys

port = int(sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', port))
sock.listen(2) # how many clients to listen to

# maintains connection forever
try:
    while True:
        print('waiting for connection')
        conn, client_addr = sock.accept()
        print(f'connection from {client_addr}')

        try:
            while True:
                data = conn.recv(1024).decode() # decode byte from client
                if data:
                    print('from client: ' + str(data))
                    # data = input('=>=> ')
                    data = 'data received'
                    conn.send(data.encode()) # encode the string into byte for client
                else:
                    break
        finally:
            conn.close()
            print('client left')
except KeyboardInterrupt:
    data = 'server is shutting down'
    print(data)
    # conn.send(data.encode())
    conn.close()

