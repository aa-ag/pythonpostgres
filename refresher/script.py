###############################################################################
# unpacking arguments

def add(x, y):
    return x + y

# numbers = [2, 2]
# excecuted = add(*numbers)
# print(excecuted)

numbers = {"x": 2, "y": 3}
excecuted = add(**numbers)
print(excecuted)