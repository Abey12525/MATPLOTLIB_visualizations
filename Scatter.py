#scatter plot
import matplotlib.pyplot as plt

population_age = [2,4,6,8,10,12,45,15,73,125,35,1,35,7,3,5,6,25,6,2,4,78,2,3,6,78,8,42,63,77,3,4,36,12,5,67,8,45]
x=[1,2,3,4,5,6,7]
y=[5,2,6,8,2,8,0]
plt.scatter(x,y,label = 'skitscat',color = 'k',marker='*',s=100)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()