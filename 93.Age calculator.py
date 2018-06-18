#Age calculator

from _datetime import date
try:
    def calculate_age(dtob):
        today = date.today()
        return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
    print()
    print(calculate_age(date(1997,10,1)))

except:
    print("Enter a val;id input!")