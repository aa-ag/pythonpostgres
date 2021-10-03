###############################################################################
# unpacking arguments

def add(x, y):
    return x + y

numbers = [2, 2]
excecuted = add(*numbers)
print(excecuted)