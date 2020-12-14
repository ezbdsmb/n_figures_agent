import socket


class UDPClient:
    def __init__(self, server_addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_addr = server_addr

    def send(self, message):
        self.sock.sendto(bytes(message, "utf-8"), self.server_addr)

    def recv(self):
        return str(self.sock.recv(1024), "utf-8")
