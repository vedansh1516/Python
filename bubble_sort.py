def sort(num):
    for i in  range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
num=[]
n=int(input("number of elements:"))
for i in range(0,n):
    ele= int(input())
    num.append(ele)
sort(num)
print(num)                