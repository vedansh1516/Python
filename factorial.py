f=int(input("enter a number to find factorial:"))
if f==0:
    print("factorial is 1")
else:
    for i in range(1,f):
        f=f*i
    print("factorial is",f)
        
