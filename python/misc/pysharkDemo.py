#!/usr/bin/python3
# coding:utf-8


import pyshark
import binascii
import base64

rfp = '/tmp/in.pcap'
wfp = '/tmp/o'
data = []
cap = pyshark.FileCapture(rfp)
# print(dir(cap[0]))
# print(dir(cap[0].highest_layer))
for pkt in cap:
    if pkt.highest_layer == "ICMP":
        if pkt.icmp.type == "0":
            if pkt.icmp.data not in data:
                data.append(pkt.icmp.data)
    if pkt.highest_layer == "ARP":
        continue

f = open("/tmp/out", "wb")
for i in data[1:-1]:
    print(i)
    f.write(base64.b64decode(binascii.unhexlify(i).decode()[8:-1].encode()))
f.close()
