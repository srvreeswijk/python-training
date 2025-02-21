import matplotlib.pyplot as plt

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none',  s=50, c='red')
#plt.scatter(2, 4, s=200)

plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()