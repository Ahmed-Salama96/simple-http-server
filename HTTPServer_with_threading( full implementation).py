from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer # to convert the response to bits 
from os import curdir, sep # to search in the server folder
from SocketServer import ThreadingMixIn
import threading

PORT = 8888
HOST = "" #local host 
#This class will handles any incoming request from the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests from browser
	def do_GET(self): 
                #Contains the request path.
		if self.path=="/":
			self.path="/home.html"
		try:
			#Check the file extension required and set the right mime type
			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
			        sendReply = True
                        if self.path.endswith(".png"):
				mimetype='image/png'
			        sendReply = True
                        if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
			       #Open the static file requested and send it
                               thread= threading.currentThread().getName()
			       f = open(curdir + sep + self.path) #open teh current directory and choose the speciefic file 
			       self.send_response(200)
			       self.send_header('Content-type',mimetype)
			       self.end_headers()
                               # wfile Contains the output stream for writing a response back to the client.
                               #self.wfile.write(thread)
		               #self.wfile.write("\n")
                               self.wfile.write(f.read())
                               f.close()
			return
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = ThreadedHTTPServer((HOST, PORT), myHandler)
	print 'Started httpserver on port ' , PORT
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'

	server.socket.close()





