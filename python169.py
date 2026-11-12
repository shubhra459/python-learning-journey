import datetime
start_date = datetime.date(2026,9,20)
duration = datetime.timedelta(days=15)
new_date = start_date - duration
print(new_date)