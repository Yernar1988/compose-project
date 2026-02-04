import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import signal, sys

MESSAGE = os.getenv("MESSAGE", "Hello from Backend!")
PORT = 5000

HOST = socket.gethostname() 

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/api"):
            body = body = f"Hello from Backend! host={HOST}".encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/health":
            body = b"OK"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

def main():
    httpd = HTTPServer(("0.0.0.0", PORT), Handler)

    def shutdown(signum, frame):
        httpd.shutdown()
        httpd.server_close()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    print(f"Backend listening on 0.0.0.0:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    main()

