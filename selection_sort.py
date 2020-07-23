def sort(num):
    for i in  range(0,len(num)-1):
        mi=i
        for j in range(i,len(num)):
            if num[j]<num[mi]:
                mi=j
        temp=num[i]
        num[i]=num[mi]
        num[mi]=temp
num=[]
n=int(input("number of elements:"))
for i in range(0,n):
    ele= int(input())
    num.append(ele)
sort(num)
print(num)                
