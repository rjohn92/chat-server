#!/usr/bin/env python3

import socket
HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))            # 1. Connect to server
    while True:
        msg = input("Enter message (Send empty string to disconnect): \nYou said:")     # 2. Get user input
        if msg =="" or not msg:
            print("Disconnecting...")
            break
        s.sendall(msg.encode())            # 3. Send message
        data = s.recv(1024)                # 4. Receive echo
        print("Server replied:", data.decode())
print("Program complete")
