import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("%uuid from tcp socekt".encode('utf-8'), ("127.0.0.1", 54321))
datarecv, addr = s.recvfrom(4096)
s.close()
print(datarecv.decode())