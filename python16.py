n = int(input("enter your number: "))
reversed = 0
while n > 0:
    don = n % 10
    digit = don
    n = n  // 10
    reversed = reversed*10 + digit
print(reversed)     
 