#!/usr/bin/env python
import socket
import threading

server_address = '0.0.0.0'
server_port = 33333

def handle_client(conn, addr):
    while True:
        msg = conn.recv(4096).decode("utf-8")
        if msg:
           msgto  = "TCP | Client address: %s:%s\nData sent by client:\n%s\n" % (
                addr[0], addr[1], msg)
           print(msgto)
           sent_tcp = conn.sendto(msgto.encode(), addr)
        else:
           break
    conn.close()

def handle_client_udp(server_udp):
    while True:
        data_udp, client_address_udp = server_udp.recvfrom(4096)
        if data_udp:
           response_udp = "UDP | Client address: %s:%s\nData sent by client:\n%s\n" % (
                client_address_udp[0], client_address_udp[1], data_udp)
           print(response_udp)
           sent_udp = server_udp.sendto(response_udp.encode(), client_address_udp)


def start():
    while True:
        conn, addr = server_tcp.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_tcp.bind((server_address, server_port))
server_tcp.listen()

server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_udp.bind((server_address, server_port))

print("Listening on " + server_address + ":" + str(server_port))

thread_udp = threading.Thread(target=handle_client_udp, args=[server_udp])
thread_udp.start()

start()
