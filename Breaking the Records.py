def breakingRecords(scores):
    ls=scores[0]
    hs=scores[0]
    hcount=0
    lcount=0
    for i in range(len(scores)):
        if(scores[i]>hs):
            hs=scores[i]
            hcount=hcount+1
                                                
    for i in range(len(scores)):
        if(scores[i]<ls):
            ls=scores[i]
            lcount=lcount+1
    print(hcount,lcount)


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)
