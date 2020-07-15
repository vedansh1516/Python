# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:56:24 2020

@author: Vedansh singhal
"""
l=[int(x) for x in input("ENTER LIST: ").split()]
c1=l.count(0)
c2=l.count(1)
if c1==1:
    print("CAN BE TURNED TO ALL 1")
    for i in range(len(l)):
        if l[i]==0:
            l[i]=1
        print(l[i],end=" ")
elif c2==1:
    print("CAN BE TURNED TO ALL 0")
    for i in range(len(l)):
        if l[i]==1:
            l[i]=0
        print(l[i],end=" ")
else:
    print("NOT POSSIBLE")


