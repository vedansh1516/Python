string=input("enter your string: ")
t= string.split(" ")
for i in range(len(t)-1,-1,-1):
    print(t[i],end=" ")