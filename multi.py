from http.server import HTTPServer , BaseHTTPRequestHandler
a = """
<!DOCTYPE html>
<html>
<head>
<title> MY WEBSERVER</title>
</head>
<body>
<h1>WELCOME TO MYFIRST WEBSERVER</h1>
<h2>LETS START !</h2>
<h3>MULTIPLICATION TABLE</h3>
11 x 0 = 0<br>
11 x 1 = 11<br>
11 x 2 = 22<br>
11 x 3 = 33<br>
11 x 4 = 44<br>
11 x 5 = 55<br>
11 x 6 = 66<br>
11 x 7 = 77<br>
11 x 8 = 88<br> 
11 x 9 = 99<br> 
11 x 10 = 110<br>
</body>
</html>
"""
class tables (BaseHTTPRequestHandler):
    def do_GET(self):
        print("WELCOME")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(a.encode())
server_address=('',80)
httpd=HTTPServer(server_address,tables)
print("WEBSERVER IS WORKING")
httpd.serve_forever()
