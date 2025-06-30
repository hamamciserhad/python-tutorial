import socket

# create a socket

s = socket.socket()
print("Socket created")
# bind a socket
s.bind(("0.0.0.0", 8080))
s.listen(3)