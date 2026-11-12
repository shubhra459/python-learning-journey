def factorial (n):
    if n == 1:
        return 1
    ial = n * factorial(n-1)
    return ial

print(factorial(int(input("enter your number:"))))

