Age = int(input("enter your age: "))
if Age  < 18 :
    print(f" loan rejected: \n  reason:underage")
else:   
 Monthly_salary =int(input("enter your salary: "))
 if Monthly_salary >= 30000:
  
  print("loan approved")
 else:
   print("loan rejected \n reason: low salary") 