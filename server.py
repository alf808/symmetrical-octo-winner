#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(2) # how many clients to listen to

print('waiting for connection')
conn, client_addr = sock.accept()
print(f'connection from {client_addr}')

try:
    while True:
        data = conn.recv(1024).decode() # decode byte from client
        if data:
            print('from client: ' + str(data))
            data = input('=>=> ')
            conn.send(data.encode()) # encode the string into byte for client
        else:
            break

finally:
    conn.close()
    print('client left')
