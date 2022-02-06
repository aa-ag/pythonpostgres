import matplotlib.pyplot as plt

option_values = [63, 28, 8]
option_names = ["A", "B", "C"]
figure = plt.figure()
axes = figure.add_subplot()
axes.pie(
    option_values,
    labels=option_names,
    explode=[0.1, 0, 0],
    autopct="%1.1f%%"
)

plt.show()