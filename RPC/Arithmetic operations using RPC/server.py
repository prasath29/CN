from xmlrpc.server import SimpleXMLRPCServer
def is_even(n):
    return n % 2 == 0
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial
def multiply(x, y):
    return x * y
def divide(x, y):
    return x // y
# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
# Register a function under a different name
server.register_function(is_even, "is_even")
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(factorial,"factorial")
#server.register_function(factorial,"factorial")
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')
# Run the server's main loop
server.serve_forever()