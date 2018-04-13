#legends,title,labels

import matplotlib.pyplot as plt

population_age = [2,4,6,8,10,12,45,15,73,125,35,1,35,7,3,5,6,25,6,2,4,78,2,3,6,78,8,42,63,77,3,4,36,12,5,67,8,45]
#ids = [x for x in range(len(population_age))]   
bins = [0,10,20,30,40,50,60,70,80,90,100,130]
plt.hist(population_age,bins,histtype='bar',rwidth=0.8)
plt.xlabel('Bins')
plt.ylabel('population_age')
plt.title('Histogram')
plt.legend()
plt.show()