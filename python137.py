try:
 x = int(input("enter your number:"))
 don = 100/x
except ValueError as e:
 print(e)
except ZeroDivisionError:
 print("suitable msg")
finally:
 print("program finished")  