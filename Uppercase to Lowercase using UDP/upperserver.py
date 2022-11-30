import socket
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "Hello UDP Client"
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
while(1):
    message,address = UDPServerSocket.recvfrom(bufferSize)
    clientMsg = f'Message from Client:{message}'
    clientIP  = f"Client IP Address:{address}"
    print(clientMsg)
    print(clientIP)
    bytesToSend= str.encode(clientMsg.upper())
    UDPServerSocket.sendto(bytesToSend, address)