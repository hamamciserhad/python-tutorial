import socket

# Step 1: Create a socket object
server_socket = socket.socket()  # Default: AF_INET (IPv4), SOCK_STREAM (TCP), proto=0, fileno=None
print("Socket created")

# Step 2: Bind the socket to a local address (IP and port)
server_socket.bind(("localhost", 8080))

# Step 3: Set the socket to listen mode (wait for up to 3 connections)
server_socket.listen(3)
print("Socket listening")

# Step 4: Accept incoming connections in a loop
while True:
    # Wait for a client to connect (blocking)
    client_socket, addr = server_socket.accept()

    # Step 5: Receive data from the client (up to 1024 bytes) and decode it
    name = client_socket.recv(1024).decode()

    # Step 6: Print the address and the received name
    print("Got connection from", addr, "-", name)

    # Step 7: Send a response back to the client
    client_socket.send("Hello there".encode())

    # Step 8: Close the client socket
    client_socket.close()