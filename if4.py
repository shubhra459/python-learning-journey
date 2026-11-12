user_bill_amount = int(input("enter your amount---"))
if user_bill_amount >= 1000:
   discount= user_bill_amount*float(0.10)
   final_bill= user_bill_amount-discount
   print(f"original bill---{user_bill_amount},disscount {discount},final bill  {final_bill} ")
else:
    print("no discount")
    