fname = input("Enter file name: ")
fh = open(fname, "r")
for i in fh:
    c=(i.split(" "))
    c.sort()
    print(c)
