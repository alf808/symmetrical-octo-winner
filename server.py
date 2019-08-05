#!/usr/bin/python3
'''first attempt to use threading module'''
import socket
import threading
import sys

port = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', port))
sock.listen(2) # how many clients to listen to

def handle_connect(sckt):
    '''to be used as target in threading handler'''
    request = sckt.recv(1024).decode()
    print(f'recvd {request}')
    data = 'data recvd'
    sckt.send(data.encode())
    sckt.close()

# maintains connection forever
try:
    while True:
        print('waiting for connection')
        conn, client_addr = sock.accept()
        print(f'connection from {client_addr}')

        handler = threading.Thread(
            target=handle_connect,
            args=(conn,) # the args will be passed to handle_connect
        )
        handler.start()

except KeyboardInterrupt:
    data = 'server is shutting down'
    print(data)
    # conn.close()

