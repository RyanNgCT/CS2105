import socket

address = ("127.0.0.1", 8888)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(address)

while True:
    data, addr = sock.recvfrom(4096)
    print(f"{data} from {addr}")

    sock.sendto(data, addr)
