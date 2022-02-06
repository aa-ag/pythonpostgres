import matplotlib.pyplot as plt

plt.figure()
lines = plt.plot([1, 2, 3, 4], [3, 5, 7, 9])
plt.setp(lines, color='00000')
plt.show()