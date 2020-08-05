from matplotlib  import pyplot as plt
x=[5,8,10,12]
y=[12,16,6,12]
x1=[6,9,11,13]
y1=[6,15,7,19]

plt.bar(x,y,label='line one',color='r')
plt.bar(x1,y1,label='line two',color='g')
plt.ylabel("quantity")
plt.xlabel("year")
plt.title("bar graph")
plt.legend()
plt.show()