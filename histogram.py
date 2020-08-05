from matplotlib import pyplot as plt
population=[12,34,32,45,65,34,76,34,65,87,56,90,76,111,123,125,104,43,76,45,97,79,68,86]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140]
plt.hist(population,bins,histtype='bar',rwidth=0.8,color='k')
plt.ylabel("y")
plt.xlabel("x")
plt.title("histogram")
plt.legend()
plt.show()