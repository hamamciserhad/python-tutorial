import socket

# Step 1: Create a socket object
# AF_INET = IPv4, SOCK_STREAM = TCP
client_socket = socket.socket()  # Uses default parameters: AF_INET and SOCK_STREAM

# Step 2: Define server address and connect to the server
# Make sure the server is running and listening on this address and port
server_address = ("localhost", 8080)
client_socket.connect(server_address)

# Step 3: Ask the user for their name
name = input("What is your name? ")

# Step 4: Encode the name to bytes and send it to the server
client_socket.send(name.encode())

# Step 5: Receive a response from the server (up to 1024 bytes)
response = client_socket.recv(1024).decode()

# Step 6: Print the server's response
print("Server says:", response)

# Step 7: Close the connection
client_socket.close()
