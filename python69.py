numbers = [10,20,30,40,50]
def double(number):
    return number * 2
don = map(double, numbers)
don = list(don)
print(don)