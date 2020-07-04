import re
str = "hell,mell,pell,cell"
match = re.findall("[a-z]ell", str)
for i in match:
    print(i)
