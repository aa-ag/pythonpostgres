def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be 0") 
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)

result = calculate(10, 2, operator=divide)
print(result)