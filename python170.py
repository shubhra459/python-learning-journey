import datetime
order_date = datetime.date(2026,8,5)
deliver_date = datetime.date(2026,8,12)
difference = deliver_date - order_date
print(difference.days)
