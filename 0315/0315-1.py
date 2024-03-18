
# x = range(4)
# y = [i**2 for i in x]

# # plt.plot(x, y)
# # plt.scatter(x, y)

# import random 
# from random import randint
# x = ([random.randint(0, 9) for _ in range(1000)])

# plt.hist(x)
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

x1 = list(range(5))
y1 = [i**2 for i in x1]

x2 = list(range(5))
y2 = [i**3 for i in x1]

fig, ax = plt.subplots()
ax.plot(x1, y1, label = "AAA", color= "red", linewidth=5)
ax.plot(x2, y2, label = "BBB", color = "black")
ax.scatter(x1, y2)
ax.hist(x1)

ax.set_title('AAA vs BBB')
ax.set_xlabel('x1')
ax.set_ylabel('x1')

ax.set_xticks([0, 1, 2, 3, 4])

ax.xaxis.set_major_locator(MultipleLocator(1))
#ax.set_major_xxx

plt.legend()
plt.show()


