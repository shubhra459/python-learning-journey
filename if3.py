balance=int(input("enter your balance  "))
amount=int(input("enter ur ammount  "))
remaining_balance= balance - amount
if amount <= balance:
    print(f'withdrw successful   {amount} ,remaining balance{remaining_balance}')
else:
    print("insufficient balance")    