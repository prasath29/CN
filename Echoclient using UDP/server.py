from socket import *
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12000))
print("UDP server is listening")
while True: 
    message, address = server_socket.recvfrom(1024)
    print(message)
    print(address)
    server_socket.sendto("This is UDP".encode('utf-8'), address)

