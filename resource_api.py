import http.server
import socketserver


class ResourceAPIHandler(http.server.SimpleHTTPRequestHandler):
    # Define what happens when a GET request is received
    def do_GET(self):
        # Send a successful response with a 200 status code
        self.send_response(200)

        # Set the response header to indicate the content type as plain text
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Write the response
        self.wfile.write(b'Resource API: Here is your requested data.')


# Define the port on which the server will listen for incoming calls
PORT = 9000

# Create an instance of the TCP server
with socketserver.TCPServer(('', PORT), ResourceAPIHandler) as httpd:
    # Print a message indicating that the server is listening
    print(f'Serving Resource API at port {PORT}')

    # Start serving and handling incoming calls
    httpd.serve_forever()
