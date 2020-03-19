#!/usr/bin/python

import socket
import time

server_ip, server_port = "13.235.41.207", 9999
ssh_port = 22

while(True):
    try:

        # Initialize a TCP client socket using SOCK_STREAM
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_ssh = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Establish connection to TCP server and exchange data
        tcp_client.connect((server_ip, server_port))
        tcp_ssh.connect(('localhost', ssh_port))

        tcp_client.settimeout(0.01)
        tcp_ssh.settimeout(0.01)
        connected = True
        while(connected):
            try:
                connected = False
                datarecv = tcp_client.recv(1024)
                if len(datarecv) > 0:
                    tcp_ssh.send(datarecv)
                    connected = True
            except socket.timeout:
                connected = True

            try:
                connected = False
                datasend = tcp_ssh.recv(1024)
                if len(datasend) > 0:
                    tcp_client.send(datasend)
                    connected = True
            except socket.timeout:
                connected = True

    finally:
        print('Connection closed')
        tcp_client.close()
        tcp_ssh.close()


