numbers = [10,25,60,45,80,30,100]
def is_greater_than_50(number):
    return number > 50
don = filter(is_greater_than_50, numbers)
don = list(don)
print(don)