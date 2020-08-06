from matplotlib import pyplot as plt
days=[1,2,3,4,5,6,7]
sleeping=[5,2,7,4,1,8,9]
walking=[2,4,7,4,1,8,9]
eating=[5,3,7,1,9,7,6]
jogging=[1,8,5,3,9,3,7]
plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='walking',linewidth=5)
plt.plot([],[],color='r',label='eating',linewidth=5)
plt.plot([],[],color='k',label='jogging',linewidth=5)
plt.stackplot(days,sleeping,walking,eating,jogging)
colors=['m','c','r','k']

plt.ylabel("y")
plt.xlabel("x")
plt.title("stckplot")
plt.legend()
plt.show()