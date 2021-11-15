def divide(dividend, divisor):
    if divisor == 0:
        print("divisor cannot be 0")
        return 
    return dividend / divisor

divide(10, 0)


grades = list()

average = divide(sum(grades), len(grades))
print(average)