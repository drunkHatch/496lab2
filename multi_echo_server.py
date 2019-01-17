#!/usr/bin/venv python3

import socket
from multiprocessing import Process


HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handle_echo(conn, addr):
    with conn:
        print(conn)
        full_data = b""
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
        # send data back
        conn.sendall(full_data)
        # tell connection to shut read and write
        conn.shutdown(socket.SHUT_RDWR)

def main():
    # create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # use the same port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1) # make socket listen
        while True:
            conn, addr = s.accept() # acceot incoming connections
            # add more worker t o acpet connections
            p = Process(target=handle_echo, args= conn, addr)
            p.daemon = True
            p.start()
        #print(full_data)
        # send data back

if __name__ == "__main__":
    main()
