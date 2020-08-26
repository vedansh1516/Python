# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count=0
    ar.sort()
    l=len(ar)
    c=ar[l-1]
    for i in range(0,l):
        if(ar[i]==c):
            count+=1
    return count
