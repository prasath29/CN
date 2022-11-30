from xmlrpc.server import SimpleXMLRPCServer
def selection_sort(x):
    x.sort()
    return x
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(selection_sort,"selection_sort")
server.serve_forever()