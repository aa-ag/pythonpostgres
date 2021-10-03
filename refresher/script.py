###############################################################################
# unpacking arguments

# def add(x, y):
#     return x + y

# numbers = [2, 2]
# excecuted = add(*numbers)
# print(excecuted)

# numbers = {"x": 2, "y": 3}
# excecuted = add(**numbers)
# print(excecuted)

###############################################################################
# def kwa(**kwargs):
#     print(kwargs)

# kwa(string="blue", number=1, float=0.5, boolean=True)

# def kwa(string, number, float, boolean):
#     print(string, number, float, boolean)

# inputs = {'string': "blue", 'number': 1, 'float': 0.5, 'boolean': True}
# kwa(**inputs)

def combine(*args, **kwargs):
    print(args)
    print(kwargs)

combine(1, 2, 3, 4, 5, 6, 7, 8, string="hello world", boolean=False)

###############################################################################
