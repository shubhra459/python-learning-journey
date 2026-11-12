n = int(input("enter your number: "))
n1 = n
reversed = 0
while n > 0:
    don = n % 10
    
    n = n  // 10
    reversed = reversed*10 + don

if n1 == reversed :
    print(f"number is palindrom ")
else:
    print("not palindrom")    
 
