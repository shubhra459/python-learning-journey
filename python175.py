import datetime
date = input("enter your date:")
current_date =datetime.datetime.strptime(date,"%d-%m-%Y")
print(current_date.isoweekday())