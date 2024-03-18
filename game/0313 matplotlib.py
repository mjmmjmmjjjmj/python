import matplotlib.pyplot as plt
import random
fig, ax = plt.subplots()  # Create a figure containing a single axes.

data = [random.randint(0, 100) for _ in range(1000)]
ax.hist(data)
plt.show()

# def plot(x, y, label): 
#   ax.plot(x, y, label = 'blue')

# x1 = [1, 2, 3, 4]
# y1 = [2, 3, 4, 6]
# plot(x1, y1, 'blue')  # Plot some data on the axes.
# ax.scatter(x1, y1, label = 'blue')  # Plot some data on the axes.

# x2 = [1, 2, 3, 4]
# y2 = [1, 2, 3, 4]
# plot(x2, y2, 'orange')

# ax.set_title('Plot A and B')
# ax.set_aspect('equal')
# ax.set_xlabel('Age')
# ax.set_ylabel('BMI')
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)
# ax.legend() #함수호출
# plt.figsave('plot.png')
# plt.show()