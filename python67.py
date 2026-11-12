numbers = [10,15,20,25,30]
def is_even(number):
    return number % 2 == 0
don =filter (is_even ,numbers)
don= list(don)
print (don)