import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("142.250.183.206", 80))  # Google IP, HTTP
s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
print(s.recv(1024).decode())
s.close()
