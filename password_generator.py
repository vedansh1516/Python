import random
string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01233456789!@#$%^&*"
l=int(input("enter the length of password:"))
password="".join(random.sample(string,l))
print(password)