from matplotlib  import pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[5,8,10]
y=[12,16,6]
x1=[6,9,11]
y1=[6,15,7]

plt.plot(x,y,'g',label='line one',linewidth=7)
plt.plot(x1,y1,'b',label='line two',linewidth=4)
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.title("practice")
plt.legend()
plt.grid(True,color='k')
plt.show()