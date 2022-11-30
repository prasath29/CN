import sys
from socket import *
import time
start=time.time()
ECHO_PORT = 55555
BUFSIZE = 1024
host = "172.16.8.101"

addr = host, ECHO_PORT
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
print ('udp echo client ready, reading stdin')
while 1:
 line = sys.stdin.readline()
 if not line:
    break
 s.sendto(line.encode(), addr)
 data, fromaddr = s.recvfrom(BUFSIZE)
 print ('client received %r from %r' % (data, fromaddr))
 end=time.time()
 rtt=abs(start-end)
 print(f"RTT={rtt}")

