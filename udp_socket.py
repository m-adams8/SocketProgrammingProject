import socket
uuid = "76e30e8d-984a-477e-be0b-b1d820b074b8"  # Replace with the UUID from TCP client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(uuid.encode('utf-8'), ("127.0.0.1", 54321))
datarecv, addr = s.recvfrom(4096)
s.close()
print(datarecv.decode())