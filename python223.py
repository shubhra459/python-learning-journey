def sum_numbers(n):
    if n == 1:
        return 1
    sum = sum_numbers(n-1) + n
    return sum
print(sum_numbers(int(input("enter your number:"))))
