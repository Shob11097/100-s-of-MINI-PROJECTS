#Subtract five days from current date

from datetime import date, timedelta
date = date.today()-timedelta(5)
print("Current date:" ,date.today())
print("5 days before current date: ",date)