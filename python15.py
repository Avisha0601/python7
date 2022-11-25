import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [7,3,6,11,9,4,1,8,7,5]

plt.scatter(x, y, label= "stars", color="teal",
            marker= "*", s=102)

plt.xlabel('*X*')
plt.ylabel('*Y*')
plt.title('My scatter plot')

plt.legend()
plt.show()