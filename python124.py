from functools import reduce
numbers = [2,4,6,8]
result = reduce(lambda a, b: a*b,numbers)
print(result)