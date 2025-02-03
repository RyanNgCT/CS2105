import socket

address = ("127.0.0.1", 8888)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# no need to bind address in server

text = input("Enter your message: ")
sock.sendto(text.encode(), address)

data, addr = sock.recvfrom(4096)

print(f"{data.decode()} from {addr}")