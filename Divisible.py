my_list = [12, 23, 54, 102, 39, 221, 339,]

result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Numbers divisible by 13 are",result)