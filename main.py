# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from scapy.all import *

packet = rdpcap('http.cap')

print(packet)

p = packet[0]
p.show();

p3 = packet[3]
p3.show()