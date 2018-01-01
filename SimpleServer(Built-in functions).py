import http.server
import socketserver

PORT = 8881
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT),Handler)
print("Server at port ", PORT)
httpd.serve_forever()
