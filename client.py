#!usr/bin/venv python3
import socket as sk

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
HOST: {HOST}

""".format(HOST=HOST)

def connect_socket(addr):
    (family, socketype, proto, cannoname, sockaddr) = addr
    try:
        s = sk.socket(family,socketype,proto)
        s.connect(sockaddr)
        #print("connected")
        s.sendall(payload.encode())
        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
        print(full_data)

    except Exception as e:
        print("connection error")
        pass
    finally:
        s.close()
def main():
    #("HOLY SHIT")

    addr_info = sk.getaddrinfo(HOST, PORT, proto=sk.SOL_TCP)
    addr = addr_info[0]
    connect_socket(addr)
    #print(addr)
    #print(addr_info)
    #sock = sk.socket()

if __name__ == "__main__":
    main()
