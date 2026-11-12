import datetime
date = "15-8-2026"
current_date = datetime.datetime.strptime(date,"%d-%m-%Y")
current_date1 = current_date.replace(month=12)


