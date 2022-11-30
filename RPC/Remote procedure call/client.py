import xmlrpc.client
proxy= xmlrpc.client.ServerProxy('http://localhost:8000/')
while True:
 print("PRESS 1-->START || 2--> STOP ")
 c=int(input("ENTER YOUR CHOICE"))
 a=[]
 b=[]
 if c==1:
     print("ENTER THE ELEMENTS TO ADD FIRST LIST")
     print("PRESS -1 TO EXIT THIS LIST")
 while True:
     d=int(input("--->"))
     if d==-1:
        break
     a.append(d)
 print("ENTER THE ELEMENTS TO ADD SECOND LIST")
 print("PRESS -2 TO EXIT THIS LIST")
 while True:
    e=int(input("--->"))
    if e==-2:
        break
    b.append(e)
 if c==2:
     break
 print(a)
 print(b)
 print("list_length",proxy.list_length(a))
 print("list_maximum",proxy.list_maximum(a))
 print("list_minimum",proxy.list_minimum(a))
 print("list_to_set",proxy.list_to_set(a))
 print("list_concate",proxy.list_concate(a,b))
