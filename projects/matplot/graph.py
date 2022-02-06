import matplotlib.pyplot as plt

plt.figure()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('test')
lines = plt.plot([1, 2, 3, 4], [3, 5, 7, 9])
plt.setp(lines, color='00000')
plt.show()