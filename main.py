from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class MiracleHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        self.wfile.write(bytes(f"<html><body><h1>Welcome to the 1st server</h1></body></html>", "utf-8"))

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print(f"Usage:\n{sys.argv[0]} [address] [port]")
        sys.exit(1)
    
    server = HTTPServer((sys.argv[1], int(sys.argv[2])), MiracleHTTP)
    print("Ctrl+C for exit // -_- // ")
    
    server.serve_forever()