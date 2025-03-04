import socket
import threading
import os
import re
import time
import uuid
import sys
# run this script from background: nohup python -u CSE3461/Lab/lab1_s.py > out.log 2>&1 &
# nohup python3 -u lab1_s.py > out.log 2>&1 &

host = "0.0.0.0"


class tcpThread(threading.Thread):

    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.s = sock

    def run(self):

        cont = self.s.recv(4096)

        #"""
        cont = cont.decode().strip().replace(' ', "")

        m = re.match(r"^[a-z]+\.\d+$", cont, re.I)

        print(m)
        if not os.path.exists(os.path.join(os.getcwd(), "lab1")):
            os.makedirs(os.path.join(os.getcwd(), "lab1"))
            
        if (m):
            u = str(uuid.uuid4())
            with open(os.path.join(os.getcwd(), "lab1", cont), 'w') as fout:
                fout.write(u)
            self.s.send(u.encode())
        else:
            self.s.send(
                "Unrecognized lastname.# found, please try again.".encode())

        self.s.close()


class tcpServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        s = socket.socket(type=socket.SOCK_STREAM)  
        
        #host = "192.168.1.247"  
        port = 12345  
        print(f"TCP server listening: {host}:{port}")
        s.bind((host, port))  
        s.listen(5)
        while True:
            c, addr = s.accept()  
            print('Connecting address', addr)
            tcpThread(c).start()


class udpServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        s = socket.socket(type=socket.SOCK_DGRAM)  

        #host = "192.168.1.247" 

        port = 54321
        print(f"UDP server listening: {host}:{port}")
        s.bind((host, port)) 
        
        if not os.path.exists(os.path.join(os.getcwd(), "lab1")):
            os.makedirs(os.path.join(os.getcwd(), "lab1"))
            
        while True:
            cont, addr = s.recvfrom(4096)  
            print('Incoming address: ', addr, "Incoming message: ", cont)
            cont = cont.decode().strip().replace(' ', "")
            found = False
            std = ""
            
            for filename in os.listdir(os.path.join(os.getcwd(), "lab1")):
                
                with open(os.path.join(os.getcwd(), "lab1", filename),
                          'r') as fin:
                    u = fin.read().strip().replace(' ', '')
                    if (u == cont):
                        with open(os.path.join(os.getcwd(), "received.txt"),
                                  'a') as fout:
                            fout.write(f"{filename}\n")
                        found = True
                        std = filename
                        break

            if (found):
                s.sendto(
                    f"{std} has finished part 1 and part 2 at {time.asctime(time.localtime())}"
                    .encode(), addr)
            else:
                s.sendto(
                    f"{cont} is not found, please try again or start over from part 1."
                    .encode(), addr)


if __name__ == "__main__":
    tcpthread = tcpServerThread()
    tcpthread.start()
    udpthread = udpServerThread()
    udpthread.start()

    tcpthread.join()
    udpthread.join()

    os.execl(sys.executable, sys.executable, *sys.argv)
