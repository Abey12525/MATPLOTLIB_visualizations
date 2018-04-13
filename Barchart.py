#legends,title,labels

import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [4,21,5,7,2,8]
y2 = [7,2,8,23,8,4]

plt.bar(x,y,label='Bar',color='k')
plt.bar(x2,y2,label='Bar2',color='c')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bar-Chart')
plt.legend()
plt.show()