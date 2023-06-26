import http.server

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Expires', '0')
        super().end_headers()

httpd = http.server.HTTPServer(('localhost', 8000), MyHTTPRequestHandler)
httpd.serve_forever(poll_interval=0.5)
