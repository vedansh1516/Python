from matplotlib import pyplot as plt
slices=[4,7,2,1,9]
activities=['sleeping','eating','playing','walking','yawning']
cols=['c','m','r','b','g']
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0,0,0.1,0),autopct='%0.f%%')


plt.title("Pie Chart")
plt.show()