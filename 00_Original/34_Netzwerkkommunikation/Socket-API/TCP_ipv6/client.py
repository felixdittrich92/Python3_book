#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

ip = input("IP-Adresse: ")
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((ip, 50000))

try:
    while True:
        nachricht = input("Nachricht: ")
        s.send(nachricht.encode())
        antwort = s.recv(1024)
        print("[{}] {}".format(ip,antwort.decode()))
finally:
    s.close()
