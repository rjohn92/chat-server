#!/usr/bin/env python3

import socket  # [Sockets, Message Handling]

HOST = '127.0.0.1'  # [Protocol/Workflow: where to listen]
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # [Sockets]
    s.bind((HOST, PORT))    	# [Listener: binds to address/port]
    s.listen(1)             	# [Listener: ready for 1 connection]
    print(f"Server listening on", (HOST, PORT))
    conn, addr = s.accept() # [Listener: accept a client]
    with conn:
        print(f"Client connected:", addr)  # [Testing/Interaction]
        while True:
            data = conn.recv(1024)            # [Message Handling: receive bytes]
            if not data:
                print(f"No data received. Disconnecting...")
                break
            print(f"Received:", data.decode())  # [Message Handling: decode text]
            conn.sendall(data)                 # [Protocol: echo back]
            # [Shutdown: 'with' auto-closes sockets]
    print("Server shutting down connection.")

