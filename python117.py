def numbers(*args):
    total=1
    for number in args:
        total = total*number
    print(total)

numbers(2,3,4)    