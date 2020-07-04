import re
str = "hell mell pell cell"
match = re.compile("[m]ell")
str= match.sub("new",str)
print(str)