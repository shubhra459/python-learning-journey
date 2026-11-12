intial_balance = int(5000) 
choice = int(input("Choose:\n1. Check Balance\n2. Deposit\n3. Withdraw\nEnter your choice: "))

if choice == 1:
  print(f"the initial balance {intial_balance}")
elif choice == 2:
 deposit= int(input("enter your deposit amount==="))
 new_deposit = intial_balance + deposit
 print(f"your new balance==={new_deposit}")
elif choice == 3:
 withdrawal_money = int(input("enter your amount===" ))
 if withdrawal_money <= intial_balance:
   remaining_balance =  intial_balance - withdrawal_money
   print(f"the balance is {remaining_balance}")
 else:
  print("insuficient balance")


else:
 print("u are brooke")


