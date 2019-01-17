#!/usr/bin/venv python3

import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

addr_info = socket.getaddrinfo("www.google.com", 80, proto=socket.SOL_TCP)
(family, socketype, proto, cannoname, sockaddr) = addr_info[0]

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # use the same port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1) # make socket listen
        while True:
            conn, addr = s.accept() # acceot incoming
            with conn:
                # CREATE a socket
                with socket.socket(family, socketype) as proxy_end:
                    #connect
                    proxy_end.connect(sockaddr)
                    print("connected to google")

                    # grabbing the data from connected client
                    full_data = b""
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(BUFFER_SIZE)
                        if not data: break
                        full_data += data
                        conn.sendall(full_data)
                    # sending to google
                    proxy_end.sendall(full_data)
                    # get data back from google
                    recv_data = b""
                    while True:
                        data = proxy_end.recv(BUFFER_SIZE)
                        if not data:
                            break
                        recv_data += data
                    conn.sendall(recv_data)
        #print(full_data)
        # send data back

if __name__ == "__main__":
    main()
