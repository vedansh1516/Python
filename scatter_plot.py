from matplotlib import pyplot as plt
x=[1,2,6,4,10,9,8,13,11,15]
y=[5,2,6,3,7,10,11,14,8,9]
plt.scatter(x,y,label='skitscat',color='k',s=25,marker='o')
plt.ylabel("y")
plt.xlabel("x")
plt.title("scatterplot")
plt.legend()
plt.show()