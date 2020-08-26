# Complete the extraLongFactorials function below.
def extraLongFactorials(f):
    if f==0:
        print("1")
    else:
        for i in range(1,f):
            f=f*i
        print(f)
if __name__ == '__main__':
    f = int(input())

    extraLongFactorials(f)
