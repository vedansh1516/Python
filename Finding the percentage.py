if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
x = list(student_marks[query_name])
sum = 0
for i in x:
    sum += i
sum1=sum/3
print ("%.2f" % sum1)


