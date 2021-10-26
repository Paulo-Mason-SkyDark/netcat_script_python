#!/usr/bin/python
import socket
ip = raw_input("Digite o ip: ")
port = int(input("Digite a porta: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip, port)):
	print "port {} esta fechada".format(port)
else:
	print "port {} esta aberta".format(port)

