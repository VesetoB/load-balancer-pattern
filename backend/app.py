
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SERVER_NAME = os.environ.get("SERVER_NAME", "Backend")
PORT = int(os.environ.get("PORT", "8000"))

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"Hello from {SERVER_NAME}!\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

server = ThreadingHTTPServer(("0.0.0.0", PORT), RequestHandler)
print(f"{SERVER_NAME} running on port {PORT}", flush=True)
server.serve_forever()
