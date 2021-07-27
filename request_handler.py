# from http.server import BaseHTTPRequestHandler, HTTPServer
# import json

# from {module} import {function},

# class HandleRequests(BaseHTTPRequestHandler):
#     """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
#     """

#     def parse_url(self, path):
#         """parses the URL"""
#         path_params = path.split("/")
#         resource = path_params[1]

#         if "?" in resource:

#             param = resource.split("?")[1]
#             resource = resource.split("?")[0]  
#             pair = param.split("=")  
#             key = pair[0]
#             value = pair[1]

#             return ( resource, key, value )

#         else:
#             id = None

#             try:
#                 id = int(path_params[2])
#             except IndexError:
#                 pass  
#             except ValueError:
#                 pass  
#             return (resource, id)



#     def _set_headers(self, status):
#         """Sets the status code, Content-Type and Access-Control-Allow-Origin
#         headers on the response

#         Args:
#             status (number): the status code to return to the front end
#         """
#         self.send_response(status)
#         self.send_header('Content-type', 'application/json')
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.end_headers()

#     def do_OPTIONS(self):
#         """Sets the options headers
#         """
#         self.send_response(200)
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
#         self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
#         self.end_headers()

#     def do_GET(self):
#         self._set_headers(200)

#         response = {}

#         parsed = self.parse_url(self.path)

#         if len(parsed) == 2:
#             ( resource, id ) = parsed

#             if resource == "stringInURL":
#                 if id is not None:
#                     response = f"{method(id)}"
#                 else:
#                     response = f"{method()}"
#             elif resource == "stringInURL":
#                 if id is not None:
#                     response = f"{method(id)}"
#                 else:
#                     response = f"{method()}"

#         elif len(parsed) == 3:
#             ( resource, key, value ) = parsed

#             if key == "stringInURL" and resource == "stringInURL":
#                 response = method(value)
#             if key == "stringInURL" and resource == "stringInURL":
#                 response = method(value)
#             if key == "stringInURL" and resource == "stringInURL":
#                 response = method(value)
#             if key == "stringInURL" and resource == "stringInURL":
#                 response = method(value)

#         self.wfile.write(response.encode())


#     def do_POST(self): #function
#         """handles the POST function"""
#         self._set_headers(201) 
#         content_len = int(self.headers.get('content-length', 0))

#         post_body = self.rfile.read(content_len) 

#         post_body = json.loads(post_body)

#         (resource, _) = self.parse_url(self.path) 

#         new_user = None
#         new_post = None
#         new_comment = None

        
#         if resource == "users":
#             new_user = create_user(post_body)
        
#         if resource == "posts":
#             new_post = create_post(post_body)

#         if resource == "comments":
#             new_comment = create_comment(post_body)

#     def do_PUT(self):
#         """handles the PUT requests"""
#         self._set_headers(204)
#         content_len = int(self.headers.get('content-length', 0))
#         post_body = self.rfile.read(content_len)
#         post_body = json.loads(post_body)

#         (resource, id) = self.parse_url(self.path)

#         if resource == "users":
#             update_user(id, post_body)
#         if resource == "posts":
#             update_post(id, post_body)
#         if resource == "comments":
#             update_comment(id, post_body)

#         self.wfile.write("".encode())


#     def do_DELETE(self):
#         """handles DELETE functionality"""
#         self._set_headers(204)

#         (resource, id) = self.parse_url(self.path)

#         if resource == "users":
#             delete_user(id)
#         if resource == "posts": 
#             delete_post(id)
#         if resource == "comments": 
#             delete_comment(id)

#         self.wfile.write("".encode())


# def main():
#     """Starts the server on port 8088 using the HandleRequests class
#     """
#     host = ''
#     port = 8088
#     HTTPServer((host, port), HandleRequests).serve_forever()


# if __name__ == "__main__":
#     main()