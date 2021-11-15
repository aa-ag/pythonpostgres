from typing import final


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be 0")
        return 
    return dividend / divisor

divide(10, 0)


grades = list()

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("there are no grades in your list")
else:
    print(average)
finally:
    print("thank you")