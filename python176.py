import datetime
date = input("enter your date:")
current_datetime = datetime.datetime.strptime(date,"%d-%m-%Y")
current_datetime1 = current_datetime.strftime ("%d %B %Y - %A")
print(current_datetime1)