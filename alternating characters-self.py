t=[]
def alternatingCharacters(s):
    a=len(s)
    flag=0
    for i in range(0,a-1):
        if(s[i]==s[i+1]):
            flag=flag+1
    t.append(flag)
q = int(input())
for i in range(q):
    s= input()
    result = alternatingCharacters(s)
r=len(t)
for w in range(r):
    print(t[w])    



