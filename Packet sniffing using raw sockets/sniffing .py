import socket
import struct
import binascii
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
pkt = rawSocket.recvfrom(2048) 
eHeader = pkt[0][0:14]
eth_hdr = struct.unpack("!6s6s2s", eHeader) # 6 dest MAC, 6 host MAC, 2 ethType
print("ETHERNET HEADER")
print("****************")
print("Destination Address")
print(binascii.hexlify(eth_hdr[0]))
print("Source Address")
print(binascii.hexlify(eth_hdr[1]))
print("Type")
print(binascii.hexlify(eth_hdr[2]))
print("IP HEADER")
print("*********")
ipHeader = pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s", ipHeader) # 12s represents Identification, Time to Live, Protocol | Flags, Fragment Offset, Header Checksum
print ("Source IP address %s" % socket.inet_ntoa(ip_hdr[1])) # network to ascii convertion
print ("Destination IP address %s" % socket.inet_ntoa(ip_hdr[2])) # network to ascii convertion
tcpHeader = pkt[0][34:54]
tcp_hdr = struct.unpack("!HH16s", tcpHeader)
print ("Source Source Port: %s" % tcp_hdr[0])
print ("Source Destination Port: %s" % tcp_hdr[1])