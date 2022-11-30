from socket import *
client_socket = socket(AF_INET, SOCK_DGRAM)
message = "This is User Datagram Protocol"
client_socket.sendto(message.encode('utf-8'), ("127.0.0.1", 12000))
data, address = client_socket.recvfrom(1024)