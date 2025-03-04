import socket
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))
s.send("adams.2666".encode('utf-8'))
uuid=s.recv(4096)
s.close()
print("Received UUID:", uuid.decode())
 