import re
str = "hello my name is vedansh,hello again"
for i in re.finditer("hello",str):
    d=i.span()
    print(d)
