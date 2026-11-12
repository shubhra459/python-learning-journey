from functools import reduce
numbers = [5,10,15,20]
def add(a, b):
    return a + b
result = reduce(add,numbers)
print(result)
