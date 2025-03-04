# SocketProgrammingProject
Overview

This project implements a simple client-server network communication system using both TCP and UDP protocols. The server manages connections, stores user identifiers, and verifies client requests.

Files in This Project

lab1_s.py - The main server script that handles both TCP and UDP communication.

tcp_socket.py - The TCP client that sends a user identifier to the server and receives a UUID in response.

udp_socket.py - The UDP client that verifies a previously received UUID with the server.

How It Works

Server (lab1_s.py)

Starts both a TCP and a UDP server.

The TCP server listens for incoming client connections, receives a user identifier (format: lastname.#), and stores a generated UUID.

The UDP server listens for incoming messages and verifies if a given UUID exists in its records.


TCP Client (tcp_socket.py)

Connects to the server over TCP.

Sends a user identifier (e.g., adams.2666).

Receives and prints a UUID from the server.


UDP Client (udp_socket.py)

Sends a UUID (received from the TCP client) to the server via UDP.

The server checks if the UUID exists and responds with a completion message or an error message.


How to Run

Start the Server

Run the server script in the background:

nohup python3 -u lab1_s.py > out.log 2>&1 &

This ensures the server runs persistently and logs output to out.log.

Run the TCP Client

python3 tcp_socket.py

This should output a received UUID.

Run the UDP Client

Edit udp_socket.py and replace the UUID variable with the one received from the TCP client.
Then, run:

python3 udp_socket.py

Notes

Ensure that the server is running before starting the clients.

The server creates a lab1 directory to store UUIDs associated with user identifiers.

The UDP client will only verify UUIDs previously assigned by the TCP server.

Author

Massimo Adams
