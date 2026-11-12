# filter version of list comprehension
numbers = [3,7,10,14,18,21,25]
result = [ number for number in numbers if number % 2 == 0 ]
print(result)