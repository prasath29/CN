import xmlrpc.client
proxy= xmlrpc.client.ServerProxy('http://localhost:8000/') # local server
for i in range(5):
    a=int(input("Enter a number:"))
    b=int(input("Enter b number:"))
    print("%d is even?: %d" % (a, (proxy.is_even(a)))) #access XML-RPC server through proxy
    print("addition of given number is %d "%((proxy.add(a,b))))
    print("sub of given number is %d "%((proxy.sub(a,b))))
    print("factorial: %d" %((proxy.factorial(a))))
    print("factorial: %d" %((proxy.factorial(b))))
    print("Multiplication of 2 numbers is %d" %(proxy.multiply(a,b)))
    print("Division of 2 numbers is %d" %(proxy.divide(a,b)))
