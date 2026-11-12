import datetime
date = "15-08-2026"
current_time = datetime.datetime.strptime(date, "%d-%m-%Y")
print(current_time)