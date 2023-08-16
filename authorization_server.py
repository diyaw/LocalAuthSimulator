import http.server
import socketserver


# Define a custom request handler
class AuthorizationHandler(http.server.SimpleHTTPRequestHandler):
    # Define what happens when a GET request is received
    def do_GET(self):
        # Send a successful response with a 200 status code
        self.send_response(200)

        # Set the response header to indicate the content type as plain text
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Write the response content
        self.wfile.write(b'Authorization Server: You are authorized.')


# Define the port on which the server will listen for incoming calls
PORT = 8000

# Create an instance of the TCP server
with socketserver.TCPServer(('', PORT), AuthorizationHandler) as httpd:
    # Print a message indicating that the server is listening on the specified port
    print(f'Serving Authorization Server at port {PORT}')

    # Start serving and handling incoming calls
    httpd.serve_forever()
