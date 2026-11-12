import datetime
date = input("enter your date:")
today_date = datetime.datetime.strptime(date,"%d-%m-%Y")
today_date1=datetime.timedelta(days=10) 
new_date = today_date1 + today_date
print(new_date)
today_date2 = new_date.strftime("%d %B %Y - %A")
print(today_date2)
