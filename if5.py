user_age=int(input("enter your age=="))
user_is_student=input("is user is student(y/n) ==")
if user_age < 12 :
    print("price is 100")


elif user_age  >= 12 and user_age <= 60 :
    
    if user_is_student == "y":    
     print("ticket price is 150")
    else:
     print("ticket price is 200")


else:
 print('ticket price 500') 
        