from datetime import datetime, timedelta

today_date = datetime.today()
new_today_date = today_date.strftime("%d/%m/%Y")
next_date = (today_date + timedelta(10)).strftime("%d/%m/%Y")
print(today_date)
print(new_today_date)
print(next_date)

#
# print(datetime.today())  #print today's date time
# new_date = datetime.today() + timedelta(10)
# print (new_date) #print new date time after addition of days to the current date
