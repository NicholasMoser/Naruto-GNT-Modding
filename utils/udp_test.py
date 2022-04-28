# Sends a UDP packet to GNTool's SEQ Listener for testing
import socket
UDP_IP = "localhost"
UDP_PORT = 12198
MESSAGE = "Hello, World!"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
