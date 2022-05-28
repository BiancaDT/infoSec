# This is a sample Python script for packet reading

from scapy.all import *

#read
packet = rdpcap('http.cap')

print(packet)

#show index of packet
p = packet[0]
p.show();

p3 = packet[3]
p3.show()

#change port to alternative TCP port
p[TCP].dport = 8080
p.show()

#test of packet creation
p0 = IP(dst="8.8.8.8")/TCP(dport=53)
p0.show()

p0