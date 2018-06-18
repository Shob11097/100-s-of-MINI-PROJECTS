#Try to print the current date and find the last tuesday

from datetime import date,timedelta
today = date.today()
date = date.today()
print("Current date: ",date.today())
formula = (today.weekday()-1)%7
last_tuesday = today - timedelta(days=formula)
print(last_tuesday)