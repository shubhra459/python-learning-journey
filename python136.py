
try:
 x = int(input("entr your number:"))
 don = 100/x
except ZeroDivisionError:
 print("invalid")
else:
 print(f"valid{don}") 
finally:
 print("program finished" ) 
