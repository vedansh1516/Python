#!/bin/python3

import os
import sys

def timeConversion(s):
    x=int(s[0:2])
    x=x+12
    if(s[8:10]=="AM" and x!=24):
        x=int(s[0:2])
    elif(x==24 and s[8:10]=="PM"):
        x=12
    elif(x==24):
        x=0
    print("{:0>2d}".format(x),end="")
    print(s[2:8])                                            
                                        
                                           
s = input()
result = timeConversion(s)