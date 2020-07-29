from array import*
n= int(input("enter the length of array"))
low = 0
high = n-1
mid=low+high/2
arr = array('i',[n])
print("enter values")
for i in range(n):
    x= int(input())
    arr.append(x)
key = arr[mid]
y = int(input("enter the value to be searched"))
pos = -1
def binary():
    if(y==key):
        pos = mid
        print("element found at position: ",pos)
    elif(y<key):
        high = mid=1



