from xmlrpc.server import SimpleXMLRPCServer
def list_length(a):
 return len(a)
def list_maximum(a):
 return max(a)
def list_minimum(a):
 return min(a)
def list_to_set(a):
 f=list(set(a))
 return f
def list_concate(a,b):
 return a+b
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(list_length,"list_length")
server.register_function(list_maximum, "list_maximum")
server.register_function(list_minimum, "list_minimum")
server.register_function(list_to_set, "list_to_set")
server.register_function(list_concate, "list_concate")
server.serve_forever()
