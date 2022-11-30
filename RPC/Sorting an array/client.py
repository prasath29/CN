import xmlrpc.client
proxy= xmlrpc.client.ServerProxy('http://localhost:8000/')
while True:
 print("PRESS 1-->START || 2--> STOP ")
 c=int(input("ENTER YOUR CHOICE"))
 a=[]
 if c==1:
     print("ENTER THE ELEMENTS TO ADD FIRST LIST")
     print("PRESS -1 TO EXIT THIS LIST")
 while True:
     d=int(input("--->"))
     if d==-1:
        break
     a.append(d)
 print(a)
 print(proxy.selection_sort(a))