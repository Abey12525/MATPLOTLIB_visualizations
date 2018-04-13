#loading data 
import matplotlib.pyplot as plt
import csv
import numpy as np 

x = []
y = []
r = []
z = []
with open('example.txt','r') as csvfile:
	plots = csv.reader(csvfile,delimiter = ',')
	for row in plots:
		r.append(int(row[0]))
		z.append(int(row[1]))
		
		
x,y= np.loadtxt('example.txt', delimiter=',' ,unpack=True)

plt.plot(x,y,label='Load Data from File')	
plt.xlabel('X')
plt.ylabel('Y')
plt.title('import test')
plt.legend()
plt.show()

