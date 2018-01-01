import socket
import socketserver
import os
HOST, PORT= '', 8000
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print("listening on port %s " % PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)
    if os.path.isfile(request):
        #http_response = request
        http_response = "Hello world, this is my own web server! by python 3.6"
        client_connection.sendall(bytes(http_response.encode('utf-8:')))
    else:
        client_connection.sendall(bytes("404! file not found".encode('utf-8:')))
    client_connection.close()

