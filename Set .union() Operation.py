n1=input()
l1= set(map(int,input().split()))
n2=input()
l2= set(map(int,input().split()))
print(len(l1.union(l2)))