#!/usr/bin/venv python3

import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # use the same port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1) # make socket listen
        while True:
            conn, addr = s.accept() # acceot incoming connections
            full_data = b""
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if not data: break
                    full_data += data
                    conn.sendall(full_data)
        #print(full_data)
        # send data back

if __name__ == "__main__":
    main()
