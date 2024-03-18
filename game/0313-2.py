import matplotlib.pyplot as plt

x = list(range(1, 101))
square = [i**2 for i in x]

fig, ax = plt.subplots()
plt.scatter (x, square, c=square, cmap = plt.cm.Blues)
plt.colorbar()
plt.savefig('colorbar.png')
# ax.set_title ('Square')
# ax.set_xlabel('X')
# ax.set_ylabel ('Y')
# ax.tick_params(labelsize=10)
# plt.style.use('dark_background')
# for s in plt.style.available:
#     print(s)
plt.show()