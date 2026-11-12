n = int(input("enter your number"))
original = n
total = 0
while n>0 :
    digit = n % 10
    total = total + (digit**3)
    n = n // 10
if original == total:
 print("armstrong")
else :
   print("not armstrong")     